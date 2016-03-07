import random
from random import randint

import ReadText as rt


thesaurus = {}
thesaurus.update({'Strong':['Strong', 'Able', 'Active', 'Big',
                    'Energy', 'Firm',
                    'Force', 'Heavy', 'Robust', 'Secure',
                    'Solid', 'Stable', 'Steady',
                    'Tough', 'Vigor', 'Might',
                    'Rugged', 'Sound', 'Ready', 'Alert',
					'Power', 'Powerful', 'Worthy', 'Alive',
					'Flow', 'Effect', 'Going', 'Mobile',
					'Push', 'Roll', 'Rush', 'Huge',
					'Full', 'Vast', 'Size', 'Crowd',
					'Whopper', 'Monster', 'Spirit', 'Vital',
					'Intense', 'Alpha', 'Drive', 'Life',
					'Enterprise', 'Fire', 'Force', 'Go',
					'Juice', 'Pep', 'Potent', 'Punch', 
					'Kick', 'Zip', 'Zing', 'Zest', 'Zeal',
					'Viva', 'Thick', 'Concrete', 'Set', 
					'Hard', 'Effort', 'Violence', 'Arm',
					'Draft', 'Impact', 'Pow', 'Potential',
					'Steam', 'Stress', 'Tension', 'Booming',
					'Hearty', 'Built', 'Fit', 'Lust', 'Wicked',
					'Zippy', 'Snap', 'Roar'
					]})

thesaurus.update({'Fast':['Fast', 'Agile', 'Brisk', 'Hot', 'Quick',
                  'Rapid', 'Swift', 'Accel', 'Active',
                  'Dash', 'Flash', 'Fly', 'Race', 'Snap',
                  'Wing', 'Streak', 'Time', 'Chop', 'Jiffy',
                  'Split', 'Bat', 'Crazy', 'Double', 'Scream',
                  'Sonic', 'Super', 'Ball', 'Speed', 'Haste',
				  'Nimble', 'Winged', 'Pronto', 'Presto',
				  'Energy', 'Lively', 'Sharp', 'Prompt',
				  'Trigger', 'Zip', 'Zippy', 'Draw', 'Spry',
				  'Alert', 'Busy', 'Animated', 'Red', 'Sizzle',
				  'Scorch', 'Burn', 'Burning', 'Fever',
				  'Fiery', 'Smoking', 'Hurry',
				  'Going', 'Head', 'Asap', 'Double', 'Triple',
				  'Break', 'Express', 'Ready'
				  
				  ]})

thesaurus.update({'Cute':['Cute', 'Kind', 'Nice', 'Happy', 'Great',
                  'Fun', 'Charm', 'Charming', 'Pretty',
                  'Adorable', 'Pleasant', 'Delight', 'Love', 'Loving',
                  'Soft', 'Fair', 'Admire', 'Gentle', 'Nifty',
                  'Polite', 'Glad', 'Live', 'Bliss', 'Flying',
                  'Light', 'Jolly', 'Peppy', 'Sunny', 'Perky',
                  'Tickle', 'Peace', 'Cheer', 'Enjoy', 'Merry',
                  'Magic', 'Beauty', 'Glamour', 'Grace', 'Spell',
                  'Cozy', 'Comfy', 'Silk', 'Smooth', 'Cream',
                  'Easy', 'Cushion', 'Fine', 'Furry', 'Snug',
                  'Round', 'Emotion', 'Friend', 'Like', 'Style',
                  'Ease', 'Elegant', 'Safe', 'Rest', 'Touch']})

thesaurus.update({'Social':['Social', 'Post', 'App', 'Share', 'Like',
                            'Friend', 'Message', 'Vote', 'Comment', 'Link',
                            'Friends', 'Messages', 'Shares', 'Votes',
                            'Viral', 'Photo', 'Video', 'Selfie', 'Status',
                            'Group', 'Collect', 'Common', 'Community',
                            'Nice', 'General', 'Panel', 'Play', 'Value',
                            'Part', 'Stake', 'Bite', 'Lot', 'Piece',
                            'Point', 'Points', 'Drag', 'Claim', 'Taste',
                            'Slice', 'Interest', 'Allied', 'Ally', 'Close',
                            'Same', 'Double', 'Twin', 'Near', 'Local',
                            'Buddy', 'Cousin', 'Partner', 'Class',
                            'Pal', 'Mate', 'Kick', 'Side', 'Chum', 'Crony',
                            'Room', 'Uni', 'College', 'Universe', 'Info',
                            'Letter', 'Memo', 'News', 'Note', 'Notice',
                            'Report', 'Word', 'Dope', 'Paper', 'Wire',
                            'Intel', 'Tally', 'Choice', 'Poll',
                            'Refer', 'Wish', 'Yea', 'Aye', 'Nay', 'Remark',
                            'Discuss', 'Judge', 'Buzz', 'Feed', 'Crack',
                            'Gloss', 'Input', 'Review', 'Wise', 'Hear',
                            'Network', 'Channel', 'Contact', 'Hookup',
                            'Element', 'Knot', 'Tie', 'Bond', 'In', 'Link',
                            'Linked', 'Attach', 'Relation', 'Joint', 'Nexus',
                            'Loop', 'Ring', 'Energy', 'Thrive', 'Grow',
                            'Growing', 'Picture', 'Image', 'Sketch', 'Shot',
                            'Design', 'Figure', 'Plate', 'Tail', 'Paint',
                            'Painting', 'Broad', 'Cast', 'Program', 'Tele',
                            'TV', 'Other', 'Quality', 'Rating', 'Grade',
                            'Mode', 'Stage', 'Footing', 'Degree', 'Body',
                            'Band', 'Club', 'Gang', 'Troop', 'Crowd', 'Party',
                            'Batch', 'Bunch', 'Lot', 'Crew', 'Trust', 'Set',
                            'Combo', 'Combine', 'Save', 'Stamp', 'Heap',
                            'Flock', 'Rally', 'Board', 'Nation', 'Colony',
                            'Turf', 'Public', 'People', 'Herd', 'Mob',
                            'Okay', 'Fair', 'Good', 'Swell', 'Forum',
                            'Jury', 'Town', 'Region', 'Border', 'Amigo',
                            'Sis', 'Bro', 'Cuz', 'Warn', 'Story', 'Cable',
                            'Rumor', 'Data', 'Expert', 'Umpire', 'Warden',
                            'Bench', 'Honor', 'Toss', 'Fling',
                            'Tind', 'Lob', 'Pitch', 'Line', 'Face', 'Book',
                            'Tape', 'Belt', 'Circle', 'Hoop', 'Rope', 'Stay',
                            'Strap', 'Cord', 'Join', 'Mutual', 'Urban',
                            'Free', 'Clip', 'Fuse', 'Fusion', 'Pair', 'Lock',
                            'Wed', 'Touch', 'Look', 'Top', 'Clock', 'Smirk',
                            'Profile', 'Dial', 'Form', 'Sketch'
                          ]})

thesaurus.update({'Home':['Home']})

def create_thesaurus_name():
    ENTRIES = 25
    describe_projects = {}
    words = rt.read_text('txt/words.txt')

    #Add random as a thesaurus mapping
    random_list = []
    for i in range(ENTRIES):
        random_name = ""
        random_name = random.choice(words) + random.choice(words)
        random_list.append(random_name)
    describe_projects.update({"Random":random_list})

    for entry in thesaurus:
        user_word = entry
        project_list = []
        for i in range(ENTRIES):
            project_name = ""
            generic_word = random.choice(words)
            thesaurus_word = random.choice(thesaurus[user_word])
            order = randint(0,1)
            if order == 0:
                project_name = generic_word + thesaurus_word
            elif order == 1:
                project_name = thesaurus_word + generic_word
            project_list.append(project_name)
        describe_projects.update({entry:project_list})

    return(describe_projects)


