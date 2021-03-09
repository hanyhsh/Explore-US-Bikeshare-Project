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
    cities= ["chicago", "new york city", "washington"]
    city= input("Choose one of the cities chicago, new york city or washington: ").lower().strip()
    while city not in cities:
        print("You Must Choose a Correct City!")
        city= input("Choose one of the cities chicago, new york city or washington: ").lower().strip()

    # TO DO: get user input for month (all, january, february, ... , june)
    months= ["January","February", "March", "April","May","June", "All" ]
    month= input("Choose month (january, february, ... , june) or type all for all months: ").title().strip()
    while month not in months:
        print("Not a correct choice Try Again!")
        month = input("Choose month (january, february, ... , june) or type all for all months: ").title().strip()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days= ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "All" ]
    day= input("Choose day of the week full name (monday, tuesday, ..) or type all for all days: ").title().strip()
    while day not in days:
        print("Not a correct choice Try Again!")
        day= input("Choose day of the week (monday, tuesday, ..) or type all for all days: ").title().strip()

    print('-'*90)
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
    # import data
    df = pd.read_csv(CITY_DATA[city])
    
    #parse start time
    import datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['month_name'] = df['Start Time'].dt.month
    df['day_name'] = df['Start Time'].dt.weekday_name

    # change months to string
    templist = []
    months_list = {1: "January",2:"February", 3:"March", 4:"April",5:"May",6:"June"}
    for i in df['month_name']:
        if i in months_list.keys():
            templist.append(months_list[i])
    df['month_name'] = templist
    
    if month != 'All':
        df = df[df['month_name'] == month]
    
    if day != 'All':
        df = df[df['day_name'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    f_month = df['month_name'].mode()
    print("the most common month of travel is {}.".format(f_month[0]))

    # TO DO: display the most common day of week
    f_day = df['day_name'].mode()
    print("the most common day of travel is {}.".format(f_day[0]))

    # TO DO: display the most common start hour
    f_hour = df['hour'].mode()
    if f_hour[0] > 12:
        f_hour -=12
        print("the most common hour of travel is {}pm.".format(f_hour[0]))
    elif f_hour[0] < 12:
        print("the most common hour of travel is {}am.".format(f_hour[0]))
    elif f_hour[0] == 12:
        print("the most common hour of travel is midnight.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start= df['Start Station'].mode()[0]
    nmost_common_start= df['Start Station'].value_counts()
    print('The most commonly used start stations is {} ({} times). '.format(most_common_start,nmost_common_start[0]))
  

    # display most commonly used end station
    most_common_End= df['End Station'].mode()[0]
    nmost_common_End= df['End Station'].value_counts()
    print('The most commonly used end stations is {} ({} times). '.format(most_common_End, nmost_common_End[0] ))
    
    # display most frequent combination of start station and end station trip
    start_and_end = "From " + df['Start Station'] + " To " + df['End Station']
    most_common_start_end= start_and_end.mode()[0]
    nmost_common_start_end= start_and_end.value_counts()
    print('The most frequent combination of start station and end station trip is {} ({} times).'.format(most_common_start_end,nmost_common_start_end[0] ))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    
    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    hours = total_travel_time // (60*60)
    minutes = (total_travel_time % (60*60)) // 60
    seconds = int((total_travel_time % (60*60)) % 60)
    print('The Total trips duration is {} hours {} minutes {} seconds.'.format(int(hours),int(minutes),int(seconds)))
    
    
    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    hoursm = average_travel_time // (60*60)
    minutesm = (average_travel_time % (60*60)) // 60
    secondsm = int((average_travel_time % (60*60)) % 60)
    print('The average trips duration is {} hours {} minutes {} seconds.'.format(int(hoursm),int(minutesm),int(secondsm)))
    
    # the longest trip is
    longest_trip = df['Trip Duration'].max()
    lhourm = longest_trip // (60*60)
    lminutem = (longest_trip % (60*60)) // 60
    lsecondsm = int((longest_trip % (60*60)) % 60)
    print('The longest single trip duration is {} hours {} minutes {} seconds.'.format(int(lhourm),int(lminutem),int(lsecondsm)))
    
    # the shortest trip is
    shortest_trip = df['Trip Duration'].min()
    shourm = shortest_trip // (60*60)
    sminutem = (shortest_trip % (60*60)) // 60
    ssecondsm = int((shortest_trip % (60*60)) % 60)
    print('The shortest single trip duration is {} hours {} minutes {} seconds.'.format(int(shourm),int(sminutem),int(ssecondsm)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
  
    user_types = df['User Type'].value_counts()
    print("The types of users by number of rides are: \n {} \n".format(pd.DataFrame(user_types)))
    

    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("The types of users by gender are: \n {} \n".format(pd.DataFrame(gender)))
    except:
        print("No Gender Data in this city.")
    # Display earliest, most recent, and most common year of birth
    try:
        early_year= int(df['Birth Year'].min())
        recent_year= int(df['Birth Year'].max())
        most_common_year= int(df['Birth Year'].mode())
        print('The earliest year of birth is {}, the most recent year is {}, and the most frequent year of birth is {}.'.format(early_year,recent_year,most_common_year))
    except:
        print("No Birth year Data available." )
        
        
        
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
            break


if __name__ == "__main__":
	main()