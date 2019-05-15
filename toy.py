"""
This module is a toy problem to test out genetic algorithm on the deco gene.

It assumes that a player is using Ignition and has Lvl 3 weakness exploit and Lvl 1 crit eye on his armor set.
The player also owns 1 mighty jewel, 7 attack jewels, 3 crit jewels, and 7 expert jewels, which will be used in the algorithm
Assume he has 13 lvl 3 slots

For brevity I am using the strings:
a = attack jewel
b = expert jewel
c = crit jewel
d = mighty jewel

"""
import numpy.random as npRand
import random

#maximum lvl for each skill
maxSkills = {"a": 7,
             "b": 7,
             "c": 3,
             "d": 3}
maxSlots = 2

class Build(object):
    def __init__(self, gene):
        self.gene = gene
        self.objValue = 0
        self.skills = {"b": 1} # one level of crit eye on armor
        self.baseAtt = 1104/4.8
        self.baseAff = 0.50
        self.baseCrit = 1.25 
        self.phenotype = []

    def expressGene(self):
        #print("hello world")
        for deco in self.gene:
            #print(deco)
            # if skill level is 0 < maxSkill level
            if not deco in self.skills:
                self.phenotype.append(deco)
                self.skills[deco] = 1
            elif self.skills[deco] < maxSkills[deco]:
                self.phenotype.append(deco)
                self.skills[deco]+=1

            if len(self.phenotype) == maxSlots:
                break 

    def mutate(self):
        # 50% chance to mutate the gene
        if random.randint(0,2) > 0:
            return
        
        #If we do mutate, randomly select two decos in the gene
        (r1, r2) = random.sample(range(0, len(self.gene)), 2)
        #switch the decos in the gene
        self.gene[r2], self.gene[r1] = self.gene[r1], self.gene[r2]

    def getAtt(self):
        if "a" in self.skills:
            return self.skills["a"]*3 + self.baseAtt
        else:
            return self.baseAtt

    def getAff(self):
        decoAff = 0
        # add attack boost contribution
        if "a" in self.skills and self.skills["a"] > 3:
            decoAff += 0.05
        # Add max might contribution
        if "d" in self.skills:
            decoAff += self.skills["d"]*0.1
        # add contribution from crit eye
        if not "b" in self.skills:
            pass
        elif self.skills["b"] < 3:
            decoAff += self.skills["b"] * 0.03
        else:
            decoAff += (self.skills["b"] * 0.05 - 0.05)

        return self.baseAff + decoAff

    def getCrit(self):
        if "c" in self.skills:
            return self.baseCrit + self.skills["c"] * 0.05
        else:
            return self.baseCrit

    def calcObj(self):
        """Obj function is calculated attack value: (attack)(1-affinity) + (attack)(affinity)(crit)"""
        self.objValue = self.getAtt()*(1.0-self.getAff()) + self.getAtt()*self.getAff()*self.getCrit()

def hybradizeGene(gene1, gene2):
    """There's gotta be a better way to write this function, but not gonna worry about it for now"""
    result = []

    dict1={}
    dict2={}

    # make a dictionary for each deco with list of indices as value
    for index, (var1, var2) in enumerate(zip(gene1, gene2)):
        if var1 in dict1:
            dict1[var1].append(index)
        else: dict1[var1] = [index]
        if var2 in dict2:
            dict2[var2].append(index)
        else: dict2[var2] = [index]

    # get average index for each deco (every respective value should be the same sized list)
    sumDict = {}
    for deco in dict1:
        sumDict[deco] = [sum(x)/2.0 for x in zip(dict1[deco], dict2[deco])]

    childGene = []
    while sumDict:
        minValue = 2.0 * len(gene2) + 1 # larger than the biggest possible sum
        #clean up entry if nothing left
        keys = sumDict.keys()
        for deco in keys:
            if not sumDict[deco]:
                del sumDict[deco]
            else:
                minDeco = min(sumDict[deco])
                if minDeco < minValue: minValue = minDeco
        #print(minValue)
        for deco, values in sumDict.iteritems():
            if minValue in values:
                childGene.append(deco)
                #print(deco)
                sumDict[deco].remove(minValue)
    return childGene

#Test hybradize Gene
gene1 = ["a"]*7 + ["b"]*7 + ["c"]*3 + ["d"]
#gene2 =  ["c"]*3 + ["d"] +  ["b"]*7 + ["a"]*7

#childGene = hybradizeGene(gene1, gene2)
#print(childGene)

# set  Base stats
#print(gene1)
#testBuild = Build(gene1)
#print(testBuild.gene)
#testBuild.expressGene()

#randGene = npRand.permutation(gene1)
#print(randGene)
#randIndv=Build(randGene)
#randIndv.expressGene()
#print(randIndv.phenotype)
#print(randIndv.skills)
#print(randIndv.getAtt())
#print(randIndv.getAff())
#print(randIndv.getCrit())
#print(randIndv.calcObj())

#### Genetic Algorithm ####
genSize = 100
generations  = []
firstGen = []

# Randomly generate 100 individuals 
for x in range(genSize):
    randIndv =Build(npRand.permutation(gene1))
    randIndv.expressGene()
    randIndv.calcObj()
    firstGen.append(randIndv)

# sort generation by fitness
firstGen.sort(key = lambda x: -x.objValue)
generations.append(firstGen)
#for indv in firstGen:
#    print(indv.objValue)

for genNumber in range(300):
    lastGen = generations[-1]
    #print("Generation: " + str(genNumber))
    # randomly decide number to keep from 20 to all of the individual in the previous generation
    toKeep = random.randint(20, len(lastGen))
    currentGen = generations[-1][0:toKeep]

    #fill any spaces by randomly crossover and mutating generations
    for x in range(genSize - toKeep):
        parent1, parent2 = random.sample(range(0, len(currentGen)), 2)
        child = Build(hybradizeGene(lastGen[parent1].gene, lastGen[parent2].gene))
        child.mutate()
        child.expressGene()
        child.calcObj()
        currentGen.append(child)

    currentGen.sort(key = lambda x: -x.objValue)
    generations.append(currentGen)

# print info on most fit individual
topDog = currentGen[0]
print("top dog")
print(topDog.gene)
print(topDog.phenotype)
print(topDog.skills)
print(topDog.getAtt())
print(topDog.getAff())
print(topDog.getCrit())
print(topDog.objValue)

print("loser test tube baby")
testGene = ["d"]+["a"]*4+["b"]*7+["c"]*3
loser = Build(testGene)
loser.expressGene()
loser.calcObj()
print(loser.gene)
print(loser.phenotype)
print(loser.skills)
print(loser.getAtt())
print(loser.getAff())
print(loser.getCrit())
print(loser.objValue)