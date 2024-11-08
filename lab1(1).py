# Name:
# Lab 1

import csv
import re
import collections

class Uni :
    ''' represents one university
        data: rank, name, country, students, ratio, top 3 fields
    '''
    def __init__(self, rank, name, country, num_of_students, ratio, top_fields):
        self._rank = rank
        self._name = name
        self._country = country
        self._num_of_students = num_of_students
        self._ratio = ratio
        self._top_fields = top_fields
   
    @property
    def get_rank(self):
        return self._rank
   
    @property
    def get_name(self):
        return self._name
   
    @property
    def get_country(self):
        return self._country
   
    @property
    def get_num_of_students(self):
        return self._num_of_students
    
    @property
    def get_ratio(self):
        return self._ratio
    
    @property
    def get_top_fields(self):
        return self._top_fields
    
    def __repr__(self):
        return f"\n{self.get_rank} {self.get_name}, {self.get_country}:\n  students: {self.get_num_of_students}, ratio: {self.get_ratio}\n  top fields: {self.get_top_fields}"
    
    
class UniRank :
    ''' stores data for universities and provides searches '''
    file_name = "uniRanks.csv"
    data =  []
    def __init__(self, num):
        if num < 1:
            raise ValueError("The number has to be greater than 1")

        self._num = num
        
        for line in self.gen(num):
            c = Uni(*self.parse(line))
            self.data.append(c)
            
        print(f"Number of universities read in: {num}")
        print("Number of universities for each country:")
        print(self.uniByCountry(self.data,num))
 
        print(self.data)
      
    def parse(self,line):
        rank = line[0]
        name = line[1]
        country = line[3]
        num_of_students = line[4]
        ratio = line[5]
        top_fields = line[6].split(',')[:3]
        return rank,name,country,num_of_students,ratio,top_fields
    
    def uniByCountry(self,data,num):
        c = collections.Counter(uni.get_country for uni in data[:num])
        result = ""
        for key, count in c.most_common():
            result += f"{key}: {count}\n"
        return result
    
    def get_container(self):
        return self.data
    
    def returnCountryName(self,name):
        newContainer = list(filter(lambda uni: uni.get_country == name, self.get_container))
        return newContainer
    
    def sortByStudentsOrRatio(self,sort,num):
        if num < 1:
            raise ValueError("The number has to be at least 1")
        key_func = (lambda uni: uni.get_num_of_students) if sort == "students" else (lambda uni: uni.get_ratio)
        newContainer = sorted(self.get_container(), key = key_func, reverse = True )
        return newContainer[:num]
        
    
    def gen(self,num):
        with open(self.file_name) as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                try:
                    int(line[0])
                    yield line
                except ValueError:
                    pass
                
                
                

  
            

# main block
r = UniRank(15)

