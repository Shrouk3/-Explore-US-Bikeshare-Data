import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    city = input('Enter the City name(chicago, new york city, washington): ')
    while city not in ['chicago', 'new york city', 'washington']:
        print('ERROR, ENTER A VALID CITY:')
        city = input('Enter the City name(chicago, new york city, washington): ')

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input('Enter the month(january,february,march,april,may,june,all):').lower()
        if month in months:
            break
        else:
            print('wrong input')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all']
    while True:
        day = input('enter_the _day(sunday,monday,tuesday,wednesday,thursday,friday,saturday,all):').lower()
        if day in days:
            break
        else:
            print('wrong input')


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
    df['Start Time'] = pd.to_datatime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january','february','march','april','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month_name()
    most_common_month = df['month'].mode()[0]
    print("Most common month is ", most_common_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day is ', most_common_day)

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("The most common start hour: {}".format(str(df['start_hour'].mode())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station is: {} ".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("The most common end station is: {}".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station'] + " " + df['End Station']
    print("The most common start and end station combo is: {}".format(df['routes'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is: {}".format(str(df['duration'].sum())))

    # TO DO: display mean travel time
    print("The mean travel time is: {}".format(str(df['duration'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User Type Stats:")
    print(df['User Type'].value_counts())

     #TO DO: Display counts of gender
    if city != 'washington':
        print("Gender Stats:")
        print(df['Gender'].value_counts().to_frame())

        # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest birth year is: {}".format(str(int(df['Birth Year'].min()))))
        print("The most common year is: {}".format(str(int(df['Birth Year'].mode()[0]))))
        print("The most recent year is: {}".format(str(int(df['Birth Year'].max()))))
    else:
        print('There is no data for this city')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_data(df):
    print('raw data is available to check')
    index=0
    user_input = input('Would you like to display 5 rows of row data?').lower()
    if user_input not in ['yes','no']:
        print('That\'s invalid input')
        user_input = input('Would you like to display 5 rows of row data?').lower()
    elif user_input != 'yes':
        print('thanks')
    else:
        while index+5 < df.shape[0]:
            print(df.iloc[index:index+5])
            i += 5
            user_input = input('Would you like to display 5 rows of row data?').lower()
            if user_input != 'yes':
                print('thanks')
                break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('thanks')
            break


if __name__ == "__main__":
    main()
