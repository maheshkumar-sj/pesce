def get_first(arr):
    return arr[0]
def print_all(arr):
    for item in arr:
        print(item)
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i,j)        


git config --global user.name "mahesh"
git config --global user.email "maheshgowdamahi641@gmail.com"
git config --global --list
git init
git status
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/maheshkumar-sj/pesce.git
git branch -M main
git push -u origin main