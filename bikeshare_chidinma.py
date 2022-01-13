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
    
    cities_list = ['washington', 'new york city', 'chicago']
    city = ''
    
    while city  not in cities_list:
        city = input("Tell me the city of your choice : ").lower()
        
        if city in cities_list:
            print('Nicely done!')
            
    

    # TO DO: get user input for month (all, january, february, ... , june)
    
    month_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = ''
    
    while month not in month_list:
        month = input("Tell me your choice of month from January to June :").lower()
        
        if month in month_list:
            print('Nicely done!')
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    week_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = ''
    
    while day not in week_list:
        day = input("Tell me your choice of day, or preferably all : ").lower()
        
        if day in week_list:
            print("Nicely done!")


    print('-'*40)
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
    
    df = pd.read_csv(CITY_DATA[city])


    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_the_week'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
   # TO DO: Obtain corresponding int making use of month index
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
         
   # In order to create a new dataframe, you filter by month
        df[df['month'] == month]
                                 
   # You can also filter by the day of the week to create a new dataframe
    if day != 'all':
                  
        df[df['day_of_the_week'] == day]

                  
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
                  
    month_common = df['month'].mode()[0] 
    print('The most common month:', month_common)
                  
                                 
    # TO DO: display the most common day of week
                  
    day_common = df['day_of_the_week'].mode()[0]
    print('The most common day of week:', day_common)
    

    # TO DO: display the most common start hour
                  
    start_common_hour = df['hour'].mode()[0]
    print('The most common start hour:', start_common_hour)
                  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
                  
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station:', common_start_station)              
 
                  
    # TO DO: display most commonly used end station

    common_end_station = df['End Station'].mode()[0]              
    print('The most commonly used end station:', common_end_station)
                  
    # TO DO: display most frequent combination of start station and end station trip

    start_end_station = (df['Start Station'] + df['End Station']).mode()[0]
    print('The most commonly used start and end station:', start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
                  
    time_travel = df['Trip Duration'].sum()
    print('The total time travelled:', time_travel)


    # TO DO: display mean travel time
                  
    mean_time_travel = df['Trip Duration'].mean()
    print('Displaying the mean travel time:',mean_time_travel)              


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
                  
    counts_user_types = df['User Type'].value_counts()
    print('counts of user types:', counts_user_types)

    # TO DO: Display counts of gender
                  
    if "Gender" in df.columns:
        counts_gender = df['Gender'].value_counts()
        print('counts of genders:', counts_gender)
    else:
        print('Gender not found')              

   # TO DO: Display earliest, most recent, and most common year of birth

    if "Birth Year" in df.columns:
        earliest_birth = df['Birth Year'].min()
        latest_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()
        print(" earliest, latest, and most common birth year:", earliest_birth, latest_birth, most_common_birth )
                  
    else:
        print("Not found")              


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    a = 0
    b = 5
    while True:
        display_data = input("Do you want to see the first 5 rows of data? Enter yes or no: ").lower()
        
        if display_data == "yes":
            print(df.iloc[a:b])
        df.reset_index()
        a += 5
        b += 5     
        
        if display_data == "no":
            break   


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
            break


if __name__ == "__main__":
	main()
