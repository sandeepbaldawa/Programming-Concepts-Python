# Given N things how many ways can you choose K things?
# You cannot repeat the same items
# N Choose K written as C(N,K)
# Lets say "Bob" is part of the group
# Number of way to surely pick Bob C(N-1,K-1)   ===> A
# No of ways to not include Bob in what we pick C(N-1,K) ===> B
# Total ways are A + B
