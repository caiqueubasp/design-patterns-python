
from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def __repr__(self):
        pass
    

class PersonalSection(Section):
    def __repr__(self):
        return 'Personal Section'
    
    
class AlbumSection(Section):
    
    def __repr__(self):
        return 'Album Section'
    

class ProjectSection(Section):
    
    def __repr__(self):
        return 'Project Section'
    

class PublicationSection(Section):
    
    def __repr__(self):
        return 'Publication Section'
    

class Profile(metaclass=ABCMeta):
    
    def __init__(self):
        self.sections = []
        self.create_profile()
        
    @abstractmethod
    def create_profile(self):
        pass
    
    def get_sections(self):
        return self.sections
    
    def add_section(self, section):
        self.sections.append(section)
        

class Linkedin(Profile):
        
        def create_profile(self):
            self.sections.append(PersonalSection())
            self.sections.append(ProjectSection())
            self.sections.append(PublicationSection())
            
        
class Facebook(Profile):
    
    def create_profile(self):
        self.sections.append(PersonalSection())
        self.sections.append(AlbumSection())
        
        
if __name__ == '__main__':
    profile_type = input('Qual perfil você quer criar? (Linkedin/Facebook): ')
    profile_type = eval(profile_type)()
    print(f'Criando perfil... {profile_type.__class__.__name__}')
    print(f'Perfil tem as seguintes seções: {profile_type.get_sections()}')
    