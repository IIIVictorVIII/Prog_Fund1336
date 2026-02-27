#Victor Villarreal 
#complete 
#This program takes users 5 ratings 1-10 and averages them out to a score.
#that score corresponds to a star rating that is then displayed to the user.

print('Enter 5, 1-10 ratings')

#for loop that accumilates users ratings then passes rating to determine stars function 
def main():
    TOTAL_RATING= 0

    for i in range (1,6):
        rating = float(input('Enter rating 1-10: '))
        if rating <1 or rating>10:
            print('ERROR: rating needs to be 1-10')
            rating = float(input('Enter rating 1-10: '))
        TOTAL_RATING+=rating
    score= TOTAL_RATING/5       
    
    print(f'your score of {score} gives you a rating of', determine_stars(score))
    


#criteria required for rating to earn stars
def determine_stars(num):
    if num < 5:
        return '0 stars'
    elif num < 6:
        return '*'
    elif num < 7:
        return '**'
    elif num < 8:
        return '***'
    elif num < 9:
        return '****'
    elif num > 9:
        return '*****' 


main()

   

