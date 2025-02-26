# Results (average MSE among clusters):

k=2: all converged to 1.9479966817556293\
k=4: best 1.8058587792477883; worst 3.7382580853605742 (outlier—avg 1.92)\
k=8: best 1.574205865950052; worst 1.9371392619907937\
k=16: best 1.2172697923819833; worst 1.6832984101610275\
k=24: best 0.9553471656783833; worst 1.407499633624498

There appears to be a trend of decreasing average MSE as the number of clusters increases,
however more clusters also meant there was less in-between spread of the centroids such
that the points included were forced to be closer to the centroid and there was less points
per cluster overall. There is also a likely trend of more clusters being more inconsistent.
Two clusters always converged to the same average MSE, but the observed variance between
rounds and difference between best and worst increased. There was only a single outlier for
this trend in a single round for k=4, but this could likely be attributed to poor initialization.
