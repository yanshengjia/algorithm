"""
Question:
You are on a flight and wanna watch two movies during this flight.
You are given List<Integer> movieDurations which includes all the movie durations.
You are also given the duration of the flight which is d in minutes.
Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).

Find the pair of movies with the longest total duration and return they indexes. If multiple found, return the pair with the longest movie.

Example 1:

Input: movieDurations = [90, 85, 75, 60, 120, 150, 125], d = 250
Output: [0, 6]
Explanation: movieDurations[0] + movieDurations[6] = 90 + 125 = 215 is the maximum number within 220 (250min - 30min)


Solution:
1. Brute Force
2. Hash Table
3. Sorting
"""


# Sorting
def movies_on_flight_0(durations, d):
    indexes = [i for i in range(len(durations))]
    nums = list(zip(durations, indexes))

    # sort
    nums.sort(key=lambda k:k[0])
    print(nums)

    res = [0, 0]
    max_duration = 0
    i, j = 0, len(durations) - 1
    while i < j:
        s = nums[i][0] + nums[j][0]
        print(i, j, s)
        if s <= d - 30:
            if s > max_duration:
                max_duration = s
                res[0], res[1] = nums[i][1], nums[j][1]
            i += 1
        else:
            j -= 1
    return res


if __name__ == "__main__":
    durations = [90, 85, 75, 60, 120, 150, 125]
    d = 250
    print(movies_on_flight(durations, d))
