import pandas as pd
frame = {'name':["ashi","ram","shyam","pappu","kanu"],
         'age':[20,19,18,21,22],
         'e_mail':["ashi05@gmail.com","rammu@gmail.com","shyamlal12@gmail.com","pappu03@gmail.com","kanu96@gamil.com"],
         'phone':[78455642,454564564,6566455,5545646,5455654]}
d = pd.DataFrame(frame)
print(d)
d.loc[5] = ["kaka",24,"kaka123@gmail.com",546546569]
print(d)