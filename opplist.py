# class Playlist:
#     def __init__(self,name):
#         self.name=name
#         self.songs=[]
#     def add_song(self,song):
#         self.songs.append(song)
#         print(f"Added: {song}")
#     def show_songs(self):
#         print(f"Playlist {self.name},")
#         for song in self.songs:
#             print(f" {song}")
# my_playlist =Playlist("Favorits")
# my_playlist.add_song("bohemian Rhapsody")
# my_playlist.add_song("staiway to heaven")
# my_playlist.show_songs()

class ProgramModel:
    def __init__(self,description,icon_code,id,name,popular,recommended_age,tools):
        self.description=description
        self.icon_code=icon_code
        self.id=id
        self.name=name
        self.popular=popular
        self.recommended_age=recommended_age
        self.tools=tools

class ProgramListModel:
    def __init__(self):
        self.programlist=[]

    def programAdd_List(self,program:ProgramModel):
        self.programlist.append(program)

    def __str__(self):
        return f"{self.programlist}"
        

DeveloperProgram=ProgramModel(
     "Learn industry-level software development skills, build real-world projects, and prepare for a professional developer career.",
     "developer_program",
     "ee558dfd-aa55-4a71-8c3e-46dcaf0c1863",
     "Professional Software Developer Program",
     False,
     "16-45 Years",
     [
      "Rust",
      "Dart",
      "Javascript",
      "Golang",
      "Python"
    ]
)

OfficeProgram=ProgramModel(
    "Learn essential computer skills and office tools to improve productivity and prepare for everyday work.",
    "computer_office_program",
    "d2424b15-2195-4cde-a977-e0beed7041e8",
    "Computer Basics & Office Professional Program",
    False,
    "All Ages",
    [
      "Microsoft 365 Suite",
      "Google Workspace Tools",
      "Zoom",
      "AI Productivity Tools"
    ]

)      

KidProgram = ProgramModel(
    "Fun and interactive lessons that help kids learn coding, logical thinking, and problem-solving through hands-on projects.",
    "kid_program",
    "daaa9c3d-def5-4c38-b05b-a6f07927f4c9",
    "Coding For Kid Program",
    True,
    "6-14 Years",
    [
      "Scratch",
      "Tinkercad",
      "Blockly",
      "Code.org",
      "Arduino",
      "Python",
      "BBC micro:bit"
    ]
)
CareerProgram=ProgramModel(
    "Focused training designed to prepare you with practical skills, real projects, and career readiness for a developer role.",
    "career_program",
    "2a3e6600-49bb-44cf-b743-83104ced8a07",
    "Career-Focused Developer Training Program",
    True,
    "16-45 Years",
    [
      "Visual Studio Code",
      "Git",
      "Docker",
      "Google Cloud / AWS",
      "AI Coding Tools (ChatGPT",
      "GitHub Copilot)",
      "Resume / CV",
      "LinkedIn Profile",
      "GitHub Portfolio"
    ]
)

plmodel=ProgramListModel()
plmodel.programAdd_List(DeveloperProgram)
plmodel.programAdd_List(OfficeProgram)
plmodel.programAdd_List(KidProgram)
plmodel.programAdd_List(CareerProgram)
print(plmodel)
