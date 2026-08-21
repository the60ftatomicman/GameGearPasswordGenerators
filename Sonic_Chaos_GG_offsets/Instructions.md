# How to use Aspect Editor Plus #
Aspect Editor Plus is a great tool for editing the 8-bit Sonic Games:
- Sonic 2
- Sonic Chaos
- Sonic Triple Trouble

for the Sega Master System (sms) and Sega Game Gear (gg).
These games were all built by the same developer studio (Aspect) and share very similar data structure across all 3 games.

This guide intends to help everyone get started, regardless of familiarity with editing ROMS.

# Glossary #
## Generic Terms ##
- **SMS**: Sega Master System
- **GG**: Game Gear
- **Console**: the video game system
- **ROM**: Read-only memory. It's the data stored on the physical game cartridge on the chips.
    - we never CHANGE this data while playing the game, it's just read from by the console.
    - can also be in reference to the game file. Think the `.zip` or `.gg` or `.sms` file
- **RAM**: Random Access Memory. It's memory and data stored on the physical console.
    - While playing the game this is read and written to. so that means it can change at any time!
## ROM Editing Terms ##
- **Bin**: this is in reference to the ROM file. 
    - It also refers to the `.gg` or `.sms` file that can be found in the **.zip* file of your ROM.
    - We use these 
- **Offset**: this is usually in reference to a number of bytes *offset* from the start of the *ROM* memory.
- **Index**: the assigned number of something in a list
    - usually starts at 0
- **Tile**: an 8x8 pixel image. 
    - Sometimes inappropriately called a *sprite*.
    - It's just the image data
- **Tileset**: a group of *tiles* associated with, in the case of this tool, a zone or sometimes a specific level
    - This editor focuses on level editing and not so much the sprite tiles.
- **Palette**: the only selectable colors for a given tile group (Foreground, Background)
    - tiles/sprites can't be any color, just the ones defined in our palette, of which we have *8* colors at a given time.
- **Background Palette**: Without diving into the SMS or GG hardware, lets just say these the colors that our *tilesets* will be using.
- **Foreground Palette**: Without diving into the SMS or GG hardware, lets just say these the colors that sprites can use.
## Specific to this Tool / Editing the 8-bit Sonic Games ##
- **Mappings**: What *tiles* are mapped to which *index*.
    - in other words it's where we would say a tile/sprite of a flower should have the ID of 3.
- **Level Layout**: Using the mappings and their indexes it's the way we layout our tiles to make a level.
    - I wouldn't code "put flower here" I'd code "Flower is at index 3 (our mapping) and put tile 3 here.

# Running Aspect Edit Plus #

## Pre-requisites ##
- Install the latest JRE (Java Runtime Environment)
- grab `aspectedit-<some numbers>.zip` from the github [repository](https://github.com/pixelcat-gh/aspect-edit-plus/tags)
    - ex: `aspectedit-0.6.zip`
    - extract the `.zip` to find the `.jar` file which we'll use to run things
- Fetch a `.bin` *(aka rom)* file for the desired 8-bit sonic game.
    - **Note:** if it's in a `.zip` file just unzip it for the `.gg` / `.sms` file
    - **Note:** you can use a disassembly project as well

## Simplified Instrucitons to Edit Level ##
- Run `aspectedit-<some numbers>.jar`
- Load the `Level` from `.bin`/`.sms`/`.gg`
    - do not forget to set *OFFSET*
    - Find this on the `Toolbar`, it's the **pictureframe icon**
    - offsets can be found in the config file of your games choosing.
- Load a`Palette` from `.bin`/`.sms`/`.gg`
    - do not forget to set *OFFSET* and *TYPE*
    - Find this on the `Toolbar`, it's the **rainbow circle icon**
    - offsets can be found in the config file of your games choosing.
- Load a`Tileset` from `.bin`/`.sms`/`.gg`
    - do not forget to set *OFFSET* and *COMPRESSION* and **TILECOUNT**
    - Find this on the `Toolbar`, it's the **two picture frames icon**
    - offsets can be found in the config file of your games choosing.
- Load the `Mappings` from `.bin`/`.sms`/`.gg`
    - do not forget to set *OFFSET*
    - Find this on the `Toolbar`, it's the **puzzlepiece icon**
    - offsets can be found in the config file of your games choosing.

## Detailed Instructions on Editing an Existing Level ##
*Finally*. These instructions will help guide you on every step to opening a level
in aspectedit so that we can edit it.

### Prepping for the Work ###
- Determine which game and level you want to edit.
    - under `.\docs\` in this repository, find the game config you want and **OPEN** it in notepad or something.
        - This will contain all the necessary `Offsets` and `Settings` we'll be inserting to load data.
        - **S2**     == Sonic 2
        - **CHAOS**  == Sonic Chaos
        - **TRIPLE** == Triple Trouble
        - Feature Request: Easy load via config
- Run `aspectedit-<some numbers>.jar`
    - on Windows you can just right click the icon of the `aspectedit-<some numbers>.jar` file and click *Open*

### Opening a Level ###
By the end of this we'll have our main workspace loaded. The `Level Editor` window

- Click `Level` to begin loading a level
    - Find this on the `Toolbar`, it's the **pictureframe icon**
        - *Result*: A pop-up window will appear for selecting a `.bin`/`.sms`/`.gg`
    - Find and select the appropriate `.bin`/`.sms`/`.gg` you want to edit
        - aka the ROM file
        - *NOTE* at the bottom of the popup you may need to change 'Files of Type' from **.bin** to **All File Types**
    - Find the data from the following columns in your `config` and set the following values in the pop-up
        - **"whateverLevel" -> level_layout -> "gg/sms"** should set to **offset** in the popup
    - Pick the corresponding game radio button underneath **offset**
    - Click **Open**
        - *Result*: the `Level Editor` window will open in aspectedit, and it will be a black grid
- All steps, unless in a popup for file selection, will now happen in the `Level Editor` window
- Select `Properties` which can be found on the far right, above the vertical/tall grid
    - **"whateverLevel" -> level_layout -> width** should set to **width** in the `Level Editor`
    - **"whateverLevel" -> level_layout -> height** should set to **height** in the `Level Editor`
    - **"whateverLevel" -> level_layout -> tile_offset** should set to **Tile Offset** in the `Level Editor`
    - *Result*: Nothing. However this controls how the `Level Editor` lays out the tiles once we load everything else.

*The following steps can truly be done in any order, this is just how I prefer to do it*

### Loading the Palettes ###
We need these so our tiles acutally appear as something other than black squares.
Remember, there's a `Foreground Color` and `Background Color`

- Select the **leftmost** color wheel, which is the `Foreground Color` selector
- Find and select the appropriate `.bin`/`.sms`/`.gg` you want to edit
    - aka the ROM file
    - *NOTE* at the bottom of the popup you may need to change 'Files of Type' from **.bin** to **All File Types**
    - Find the data from the following columns in your `config` and set the following values in the pop-up
        - **"whateverLevel" -> foreground_palette -> "gg/sms"** should set to **offset** in the popup
    - I just leave **Compression** selected to *Compressed*.
    - I just leave **Tile Count** as *zero*
    - TODO: I'm not entirely positive when I'd use the other options.
- Select the **rightmost** color wheel, which is the `Background Color` selector 
    - Same steps as Foreground, but use the **background_palette** offset when choosing your ROM
- *Result*: Without our tiles and mappings loaded not much. If we had our tiles loaded and mappings loaded we'd see the level display in the grid

### Loading the Tiles ###
Tiles are the 8x8 squares that build every image on screen. These are the subunits of the mappings.
4 tiles in a square == a mapping

- Select the **double picture frame**, which is the `Tileset` selector
- Find and select the appropriate `.bin`/`.sms`/`.gg` you want to edit
    - aka the ROM file
    - *NOTE* at the bottom of the popup you may need to change 'Files of Type' from **.bin** to **All File Types**
    - Find the data from the following columns in your `config` and set the following values in the pop-up
        - **"whateverLevel" -> tileset -> "gg/sms"** should set to **offset** in the popup
    - Pick the corresponding game radio button underneath **offset**
        - Note the Game Gear has a very different color selection than the SMS despite games usually sharing the same palette so this choice really matters
- *Result*: Without our mappings or palettes, nothing would show.  If we had our mappings loaded and palettes loaded we'd see the level display in the grid

### Loading the Mappings ###
Mappings are the 32x32 squares built from 4 tiles that build the foundations of a level. This I am sure was a way to save memory for more stuff.

- Select the **puzzle piece**, which is the `Mappings` selector
- Find and select the appropriate `.bin`/`.sms`/`.gg` you want to edit
    - aka the ROM file
    - *NOTE* at the bottom of the popup you may need to change 'Files of Type' from **.bin** to **All File Types**
    - Find the data from the following columns in your `config` and set the following values in the pop-up
        - **"whateverLevel" -> mapping -> "gg/sms"** should set to **offset** in the popup
- *Result*: Without our mappings or tiles, nothing would show.  If we had our tiles loaded and palettes loaded we'd see the level display in the grid
    - If you followed this guide, this is when I'd expect to see images in my grid in the level editor
    - you would also see mappings load under the `Mappings` tab. these are for editing

### Some Troubleshooting ###
- My colors are weird
    - Reload the `Palettes`
- The map looks like a mess of random tiles.
    - Most likely the **properties** aren't set
        - In the `Level Editor` select the `Properties` tab.
        - Reload the **height**,**width**, and **Tile Offset**
            - you need to click off of the input box to actually see it apply
    - If this is still incorrect and you are positive you selected the right **properties**
        - Try rerunning the process from loading the Level and working your way through the steps. An offset may be off.

## Editing the Level ##
Now that it's loaded, the editing is simple

### For the Level Layout ###
- In the `Level Editor` select the `Mappings` tab.
- Left click a **Mapping** square for the ground / background element you want to place
- Just click on the **level grid** where you want it to go.

### For Objects (Enemies/Items) ###
This is currently not a feature in aspect editor, you'll need to do this by hand.
See the guide to this under the `Editing Objects.md` file for a better understanding.
This will require you modify the actual hex code. Good luck!

## Saving Results ##
TODO