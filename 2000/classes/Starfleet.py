class Starfleet():
    def readData(self):
        speciesList = ['human', 'vulcan', 'andorian', 'tellarites']
        rankList = ['ensign', 'lieutenant',
                    'lieutenant commander', 'commander', 'captain', 'admiral']
        try:
            self.name = input('What is your name? ')
            self.species = input('What species are you? ')
            if not self.species.lower() in speciesList:
                raise Exception('You are not a member of the Federation')

            self.rank = input('What rank are you? ')
            if not self.rank.lower() in rankList:
                raise Exception(
                    'Please enter one of the following ranks: {}'.format(rankList))

            print('Hello, {0} {1} the {2}'.format(self.rank, self.name, self.species))
        except Exception as ex:
            print(ex)


Starfleet().readData()
