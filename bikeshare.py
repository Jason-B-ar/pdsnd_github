import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input("Enter City Name \n Available options are: \n chicago \n new york city \n washington: \n")
    # loop for invalid inputs on city
    while city.lower() not in ["new york city", "washington", "chicago"]:
        print ("Please input a valid city name")
        city = input("Enter City Name \n Available options are: \n chicago \n new york city \n washington: \n")

    # TO DO: get user input for month (all, january, february, ... , june)
    
    month = input(
"Enter month for filter options \n available options include \n all (for no filter)"
"\n january \n february \n march \n april \n may \n june: \n")
    # loop for invalid inputs on month
    while month.lower() not in ["all", "january", "february", "march", "april", "may", "june"]:
        print("Please input a valid month")
        month = input("Enter month for filter options \n available options include \n all (for no filter) \n january \n february \n march \n april \n may \n june: \n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input(
        "Enter day of week for filter options \n available options include"
        "\n all (for no filter) \n sunday \n monday \n tuesday \n wednesday \n thursday \n friday \n saturday: \n")
    # loop for invalid inputs on month
    while day.lower() not in ["all", "sunday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]:
              print("Please input a valid day")
              day = input("Enter day of week for filter options \n available options include \n all (for no filter) \n sunday \n monday \n tuesday \n wednesday \n thursday \n friday \n saturday: \n")    

    print('-'*40)
    
    # convert all inputs to lower text
    city = city.lower()
    month = month.lower()
    day = day.lower()
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

# loading files into dataframe
    df = pd.read_csv(CITY_DATA[city])

# change start time to a datetime 
    df['Start Time'] = pd.to_datetime(df['Start Time'])

# add month and weekday to dataframe 
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

# filter by new month field
    if month != "all":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
    
        df=df[df['month'] == month]
    
# filter by new day field 

    if day != 'all': 
        df = df[df['day'] == day.title()] 
    


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    # create new start month attribute
    # example 1:  df['start_month'] = df['Start Time'].dt.month
    df['start_month'] = df['Start Time'].dt.strftime("%B")
    
    #gather mode
    common_month = df['start_month'].mode()[0]
    
    #print mode of start_month
    print('Most common month:', common_month)

    # TO DO: display the most common day of week
    
    # create new day of week attribute
    
    df['day_week'] = df['Start Time'].dt.strftime("%A")
    
    #gather mode
    common_day = df['day_week'].mode()[0]
    
    #print mode of most common day
    print('Most common day of the week:', common_day)

    # TO DO: display the most common start hour
    
        # create new hour attribute
    
    df['hour'] = df['Start Time'].dt.hour
    
    #gather mode
    hour = df['hour'].mode()[0]
    
    #print mode of start hour
    print('Most common start hour:', hour)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

     # create new hour attribute
    
    #df['hour'] = df['Start Time'].dt.hour
    
    #gather mode
    station_mode =df['Start Station'].mode()[0]
    
    #print mode of start station
    print('Most commonly used start station:', station_mode)

    # TO DO: display most commonly used end station
    
    #gather mode
    end_station_mode =df['End Station'].mode()[0]
    
    #print mode of end station
    print('Most commonly used end station:', end_station_mode)


    # TO DO: display most frequent combination of start station and end station trip
    
        # create new combination of start station and end station
    
    df['combo_station'] = df['Start Station'] + " - " + df['End Station']
       
    #gather mode
    combo_station_mode =df['combo_station'].mode()[0]
    
    #print mode of combo station
    print('Most commonly used station combination:', combo_station_mode)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

           
    #gather sum of travel time
    travel_time =df['Trip Duration'].sum()
    travel_time_min = travel_time / 60
    
    #print mode of total travel time
    print('The total trip duration is :', travel_time_min, ' minutes')
    
    
    

    # TO DO: display mean travel time
          
    #gather average
    average_travel =df['Trip Duration'].mean()
    average_travel_min = average_travel / 60
    
    #print the average trip duration
    print('\nThe average trip duration is:', average_travel_min, ' minutes')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    # Count the number of occurances of user type
    user_type_count =df['User Type'].value_counts()
    
    
    #print the counts of each user type
    print('Counts of User Type:')
    print(user_type_count)

    # TO DO: Display counts of gender

    #start off by inputing not provided to any blank gender attributes.
    if 'Gender' in df.columns:
        df['Gender'] = df['Gender'].fillna('Not Identified')
        
         # Count the number of occurances of gender
        gender_type_count =df['Gender'].value_counts()
    
    
        #print the counts of each gender
        print('Counts of Gender:')
        print(gender_type_count)
    
    else:
        print('\nThe Gender attribute does not exist within this dataset.')
    # Count the number of occurances of gender
    #gender_type_count =df['Gender'].value_counts()
    
    
    #print the counts of each gender
    #print('Counts of Gender:')
    #print(gender_type_count)

    # TO DO: Display earliest, most recent, and most common year of birth

    #create min birth year, max birth year, and mode of the birth year
    if 'Birth Year' in df.columns:
        
        df['Birth Year'] = df['Birth Year'].dropna(axis = 0)
        
        min_by =df['Birth Year'].min()
        max_by =df['Birth Year'].max()
        mode_by = df['Birth Year'].mode()[0]
    
    
        #print the counts of each user type
        print('\nThe earliest birthday year is', min_by,)
        print('\nThe most recent birthday year is', max_by)
        print('\nThe most common birthday year is', min_by)
    else: 
        print('\nThe birth year attribute does not exist within this dataset.\n')
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            
            
            # allow users to review raw data
            
            check_data = input('Would you like to see the raw data? Enter yes or no.\n')
            if check_data.lower() != "no":
                
               
                #enter size of data    
                chunk_size= 5
                
                #create loop to keep adding more data. 
                for i in range(0, len(df), chunk_size):
                    print(df.iloc[i:i + chunk_size])
                    exit_input = input('Press Enter to see the next 5 rows, or type "Exit" to end:\n')
                    if exit_input.lower() =='exit':
                            break
                                  

            break

    

if __name__ == "__main__":
	main()
