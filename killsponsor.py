import random

# Preferences
BINDS_WANTED = 80
ADJECTIVE_CHANCE = .75
SECOND_COMPANY_CHANCE = .5


class Companies:
    """Store company data"""
    companies = None

    @classmethod
    def init(cls):
        with open("companies-fictional.txt") as f:
            c = f.readlines()
            cls.companies = map(str.strip, c)
        with open("companies-real.txt") as f:
            c = f.readlines()
            cls.companies += map(str.strip, c)

    @classmethod
    def get(cls):
        if cls.companies is None:
            cls.init()
        
        chosen = random.choice(cls.companies)
        cls.companies.remove(chosen)

        return chosen


class Text:
    score_adj = ("amazing", "impressive", "sick", "sweet", "professional", "flawless", "expert")
    score = ("kill", "frag", "ownage")
    sponsored_by = ("sponsored by", "brought to you by", "courtesy of", "paid for by")


def create_sentence():
    sentence = "This"
    
    # adjective
    if random.random() < ADJECTIVE_CHANCE:
        sentence += " " + random.choice(Text.score_adj)
    
    # append score    
    sentence += " " + random.choice(Text.score)

    # sponsored by
    sentence += " " + random.choice(Text.sponsored_by)
    
    # company
    sentence += " " + Companies.get()
   
    # decide whether to add second company
    if random.random() < SECOND_COMPANY_CHANCE:
        sentence += " and " + Companies.get()
    
    sentence += "!"

    return sentence


with open("binds.cfg", "w") as f:
    f.write('// ******************\n// Sponsored Killing\n// ******************\n')
    f.write('alias "sponsorSwitch" "sponsor1next"\n')
    f.write('alias "sponsorSay" "sponsor1say"\n')

    for i in range(1,BINDS_WANTED + 1):
        if not i == BINDS_WANTED:
            f.write('alias "sponsor{0}say" "say {1}"\n'.format(i, create_sentence()))
            f.write('alias "sponsor{0}next" "alias sponsorSay sponsor{1}say; alias sponsorSwitch sponsor{1}next"\n'.format(i, i + 1))
        else:
            f.write('alias "sponsor{0}say" "say {1}"\n'.format(i, create_sentence()))
            f.write('alias "sponsor{0}next" "alias sponsorSay sponsor1say; alias sponsorSwitch sponsor1next"\n'.format(i))
        

print "Binds saved in binds.cfg"

