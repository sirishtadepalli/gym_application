# FITNESS APP

## 1. Users
Information about the user
    - UserID
    - Username
    - Email
    - Mobile Number
    - Weight
    - Height
    - Body Fat Percentage
    - Password (Authentication later) 

## 2. Exercise
Standard exercise and their details
```
    - ExerciseID
    - ExerciseName
    - ExerciseCategory
    - ExerciseWeight
    - ExerciseSets
    - ExerciseReps
    - ExerciseIntervalSize
    - ExerciseNumberOfIntervals
```

## 3. Routines
Routines is a combination of exercises
```
    - RoutineID
    - RoutineName
    - ExerciseID
```
## 4. UserLogs
Routines the user does on a day to day basis
Example - A user logs in for MondayStrength routine for Benchpress on Monday and the following monday 
``` 
    - UserID
    - RoutineID
    - ExerciseID
    - UserDateTime
    - UserExerciseWeight
    - UserExerciseSets
    - UserExerciseReps
```


# Create a new Endpoint
1. Add equipment Endpoint to this API
1. API: Model (Table, Columns, Types)  -> Schema (Validations of inputs/output) -> Endpoint (GET, POST, PUT, DELETE) -> API (Router)
1. Database : Create table -> Insert some test data