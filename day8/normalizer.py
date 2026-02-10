import numpy as np
scores=np.random.randint(50,101,size=(5,3))
mean_scores=scores.mean(axis=0)
normalized_scores=scores-mean_scores
print("\nMean Scores(per subject):")
print(mean_scores)
print("\nNormalized Scores:")
print(normalized_scores)