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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('please enter the city you want too see data for,chicago,new york city or washington?:')

    # get user input for month (all, january, february, ... , june)
    month=input('please enter month you need to see:')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('please enter the day you need to see:')

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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month=df['month'].mode()[0]
    print('most popular month:',popular_month)

    # display the most common day of week
    popular_day_of_week=df['day_of_week'].mode()[0]
    print('most day of week:',popular_day_of_week)

    # display the most common start hour
    popular_common_start_hour=df['hour'].mode()[0]
    print('most common start hour:',popular_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_commom_start_station=df['Start Station'].mode()[0]
    print('most common start station:',most_commom_start_station)

    # display most commonly used end station
    most_common_end_station=df['End Station'].mode()[0]
    print('most common end station:',most_common_end_station)


    # display most frequent combination of start station and end station trip
    group=df.groupby['Start Station','End Station']
    most_combination_station=group.size().sort_values(ascending=false).head(1)
    print('most frequent combination of start station and end station trip:',most_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df[Trip_Duration].sum()
    print('total travel time:',total_travel_time)

    # display mean travel time
    mean_travel_time=df(Trip_Duration).mean()
    print('mean travel time:',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


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
