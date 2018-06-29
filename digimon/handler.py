# Author: Tristan Challener <challenert@gmail.com>
# Copyright: TODO

"""
Handler that stores all data to be written to the ROM.
"""

import digimon.data as data, digimon.util as util
import script.util as scrutil
from digimon.digimonclass import Digimon, Item
import random, struct
from shutil import copyfile
from future.utils import iteritems, itervalues



class DigimonWorldHandler:
    """
    Digimon World handler class.  Holds all data
    that can be modified and written out to the
    file.
    """

    #       Endianness                      Size (packed/not)
    # @     native                          native
    # =     native                          standard
    # <     little-endian                   standard
    # >     big-endian                      standard
    # !     network (= big-endian)          standard

    #       Type
    # x     pad byte
    # c     char
    # b     signed char
    # B     unsigned char
    # ?     _Bool
    # h     short
    # H     unsigned short
    # i     int
    # I     unsigned int
    # l     long
    # L     unsigned long
    # q     long long
    # Q     unsigned long long
    # f     float
    # d     double
    # s     char[]
    # p     char[]
    # P     void *

    digimonIDFormat   = '<B'
    techIDFormat      = '<B'
    animIDFormat      = '<B'
    chestItemFormat   = '<BB'
    digimonDataFormat = '<20sihh23Bx'
    itemDataFormat    = '<20sIHHb?2x'

    def __init__( self, filename ):
        """
        Load ROM data into cache so that it can be read
        and manipulated.

        Keyword arguments:
        filename -- Name of file to read.
        """

        self.inFilename = filename

        with open( filename, 'r' + 'b' ) as file:
            #------------------------------------------------------
            # Read in digimon data
            #------------------------------------------------------

            #Read in full digimon stats data block
            data_read = util.readDataWithExclusions( file,
                                                     data.digimonDataBlockOffset,
                                                     data.digimonDataBlockSize,
                                                     data.digimonDataExclusionOffsets,
                                                     data.digimonDataExclusionSize )

            #Parse data block
            data_unpacked = util.unpackDataArray( data_read,
                                                  self.digimonDataFormat,
                                                  data.digimonDataBlockCount )

            #Store data in digimon objects
            self.digimonData = []
            for i, data_tuple in enumerate( data_unpacked ):
                self.digimonData.append( Digimon( i, data_tuple ) )
                print( str( self.digimonData[ i ] ) + '\n' )


            #------------------------------------------------------
            # Read in item data
            #------------------------------------------------------

            #Read in full item data block
            data_read = util.readDataWithExclusions( file,
                                                     data.itemDataBlockOffset,
                                                     data.itemDataBlockSize,
                                                     data.itemDataExclusionOffsets,
                                                     data.itemDataExclusionSize )

            #Parse data block
            data_unpacked = util.unpackDataArray( data_read,
                                                  self.itemDataFormat,
                                                  data.itemDataBlockCount )

            #Store data in item objects
            self.itemData = []
            for i, data_tuple in enumerate( data_unpacked ):
                self.itemData.append( Item( i, data_tuple ) )
                print( str( self.itemData[ i ] ) )


            #------------------------------------------------------
            # Read in first starter data
            #------------------------------------------------------

            #Read in first starter digimon ID
            file.seek( data.starter1SetDigimonOffset, 0 )
            self.starter1ID = struct.unpack( self.digimonIDFormat, file.read( 1 ) )[0]
            print( self.digimonData[ self.starter1ID ].name )

            #Read in first starter learned tech ID
            file.seek( data.starter1LearnTechOffset, 0 )
            self.starter1Tech = struct.unpack( self.techIDFormat, file.read( 1 ) )[0]
            print( '0x' + format( self.starter1Tech, '02x' ) + ' = tech ID' )

            #Read in first starter learned tech slot
            file.seek( data.starter1EquipAnimOffset, 0 )
            self.starter1TechSlot = util.animIDTechSlot( struct.unpack( self.animIDFormat, file.read( 1 ) )[0] )
            print( '0x' + format( self.starter1TechSlot, '02x' ) + ' = tech slot' )


            #------------------------------------------------------
            # Read in first starter data
            #------------------------------------------------------

            #Read in second starter ID
            file.seek( data.starter2SetDigimonOffset, 0 )
            self.starter2ID = struct.unpack( self.digimonIDFormat, file.read( 1 ) )[0]
            print( self.digimonData[ self.starter2ID ].name )

            #Read in second starter learned tech ID
            file.seek( data.starter2LearnTechOffset, 0 )
            self.starter2Tech = struct.unpack( self.techIDFormat, file.read( 1 ) )[0]
            print( '0x' + format( self.starter2Tech, '02x' ) + ' = tech ID' )

            #Read in second starter learned tech slot
            file.seek( data.starter2EquipAnimOffset, 0 )
            self.starter2TechSlot = util.animIDTechSlot( struct.unpack( self.animIDFormat, file.read( 1 ) )[0] )
            print( '0x' + format( self.starter2TechSlot, '02x' ) + ' = tech slot' )


            #------------------------------------------------------
            # Read in chest item data
            #------------------------------------------------------

            self.chestItems = {}

            for ofst in data.chestItemOffsets:
                file.seek( ofst, 0 )
                cmd, item = struct.unpack( self.chestItemFormat, file.read( 2 ) )
                if( cmd != scrutil.spawnChest ):
                    print( 'Error: Looking for chest item, found incorrect command: ' + str( cmd ) + ' @ ' + format( ofst, '08x' ) )
                else:
                    self.chestItems[ ofst ] = item

            for item in itervalues( self.chestItems ):
                print( 'Chest contains: \'' + self.itemData[ item ].name + '\'' )


    def write( self, filename, verbose=False ):
        """
        Write all ROM data back to binary file.

        Keyword arguments:
        filename -- Output file name.
        """

        #If we have a different destination file, create a copy to edit
        if( self.inFilename != filename ):
            copyfile( self.inFilename, filename )

        with open( filename, 'r+' + 'b' ) as file:
            #------------------------------------------------------
            # Write out digimon data
            #------------------------------------------------------

            #Pack digimon data into buffer
            data_unpacked = []
            for digi in self.digimonData:
                data_unpacked.append( digi.unpackedFormat() )

            data_packed = util.packDataArray( data_unpacked, self.digimonDataFormat )

            #Set all digimon data
            util.writeDataWithExclusions( file,
                                          data_packed,
                                          data.digimonDataBlockOffset,
                                          data.digimonDataBlockSize,
                                          data.digimonDataExclusionOffsets,
                                          data.digimonDataExclusionSize )


            #------------------------------------------------------
            # Write out item data
            #------------------------------------------------------

            #Pack digimon data into buffer
            data_unpacked = []
            for item in self.itemData:
                data_unpacked.append( item.unpackedFormat() )

            data_packed = util.packDataArray( data_unpacked, self.itemDataFormat )

            #Set all digimon data
            util.writeDataWithExclusions( file,
                                          data_packed,
                                          data.itemDataBlockOffset,
                                          data.itemDataBlockSize,
                                          data.itemDataExclusionOffsets,
                                          data.itemDataExclusionSize )


            #------------------------------------------------------
            # Write out first starter data
            #------------------------------------------------------

            #Set digimon ID for first starter
            util.writeDataToFile( file,
                                  data.starter1SetDigimonOffset,
                                  struct.pack( self.digimonIDFormat, self.starter1ID ),
                                  verbose )

            #Set digimon ID to check when learning first
            #starter's first tech (must match starter!)
            util.writeDataToFile( file,
                                  data.starter1ChkDigimonOffset,
                                  struct.pack( self.digimonIDFormat, self.starter1ID ),
                                  verbose )

            #Set tech ID for first starter to learn
            util.writeDataToFile( file,
                                  data.starter1LearnTechOffset,
                                  struct.pack( self.techIDFormat, self.starter1Tech ),
                                  verbose )

            #Set animation ID to equip as first stater's
            #first tech
            util.writeDataToFile( file,
                                  data.starter1EquipAnimOffset,
                                  struct.pack( self.animIDFormat, util.techSlotAnimID( self.starter1TechSlot ) ),
                                  verbose )


            #------------------------------------------------------
            # Write out second starter data
            #------------------------------------------------------

            #Set digimon ID for second starter
            util.writeDataToFile( file,
                                  data.starter2SetDigimonOffset,
                                  struct.pack( self.digimonIDFormat, self.starter2ID ),
                                  verbose )

            #Set digimon ID to check when learning second
            #starter's first tech (must match starter!)
            util.writeDataToFile( file,
                                  data.starter2ChkDigimonOffset,
                                  struct.pack( self.digimonIDFormat, self.starter2ID ),
                                  verbose )

            #Set tech ID for first starter to learn
            util.writeDataToFile( file,
                                  data.starter2LearnTechOffset,
                                  struct.pack( self.techIDFormat, self.starter2Tech ),
                                  verbose )

            #Set animation ID to equip as first stater's
            #first tech
            util.writeDataToFile( file,
                                  data.starter2EquipAnimOffset,
                                  struct.pack( self.animIDFormat, util.techSlotAnimID( self.starter2TechSlot ) ),
                                  verbose )


            #------------------------------------------------------
            # Write out chest item data
            #------------------------------------------------------

            #Set item IDs in chests
            for ofst, item in iteritems( self.chestItems ):
                util.writeDataToFile( file,
                                      ofst,
                                      struct.pack( self.chestItemFormat, scrutil.spawnChest, item ),
                                      verbose )


    def randomizeStarters( self ):
        """
        Set starters to two random different rookie Digimon.
        """
        firstDigi = data.rookies[ random.randint( 0, len( data.rookies ) - 1) ]
        secondDigi = firstDigi
        while secondDigi == firstDigi:
            secondDigi = data.rookies[ random.randint( 0, len( data.rookies ) - 1 ) ]

        self.starter1ID = firstDigi
        print( 'First starter set to ' + self.digimonData[ firstDigi ].name )

        self.starter2ID = secondDigi
        print( 'Second starter set to ' + self.digimonData[ secondDigi ].name )

        self.setStarterTechs( default=True )


    def randomizeChestItems( self, allowEvo=False ):
        """
        Randomize items in chests.

        Keyword arguments:
        allowEvo -- Include or exclude evolution items from
                    the pool of items to choose from.
        """

        #for each chest, choose a random allowed item from data
        for key in list( self.chestItems ):
            randID = random.randint( 0, len( self.itemData ) - 1 )
            while( not self.itemData[ randID ].isAllowedInChest( allowEvo ) ):
                randID = random.randint( 0, len( self.itemData ) - 1 )
            pre = self.chestItems[ key ]
            self.chestItems[ key ] = self.itemData[ randID ].id
            print( 'Changed chest item from ' + self.itemData[ pre ].name + ' to ' + self.itemData[ self.chestItems[ key ] ].name )


    def setStarterTechs( self, default=True ):
        """
        Set starter techs to default techs (lowest tier tech
        learnable by default) for current starters.

        Keyword arguments:
        default -- No handling for now.  Support to be added
                   for other options (random) but that is
                   not possible now.
        """
        self.starter1Tech = util.starterTech( self.starter1ID )
        self.starter1TechSlot = util.starterTechSlot( self.starter1ID )
        print( 'First starter tech set to ' + data.techs[ self.starter1Tech ]
             + ' (' + self.digimonData[ self.starter1ID ].name + '\'s slot ' + str( self.starter1TechSlot ) + ')' )


        self.starter2Tech = util.starterTech( self.starter2ID )
        self.starter2TechSlot = util.starterTechSlot( self.starter2ID )
        print( 'Second starter tech set to ' + data.techs[ self.starter2Tech ]
             + ' (' + self.digimonData[ self.starter2ID ].name + '\'s slot ' + str( self.starter2TechSlot ) + ')' )

