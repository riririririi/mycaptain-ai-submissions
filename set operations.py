#!/usr/bin/env python
# coding: utf-8

# In[1]:


#making 2 sets with a few same elements so that the operations return non-empty sets
set1 = {5, 3, 12, 98, 42, 21, 17, 92}
set2 = {7, 92, 37, 17, 85, 38, 98, 21}


# In[2]:


print("the union of set1 and set2 is:", set1 | set2) #returns set with all the elements in both the sets without duplicates
print("the intersection of set1 and set2 is:", set1 & set2) #returns set with elements which are common in both
print("the difference of set1 and set2 is:", set1 - set2) #returns elements which are in set1 but not in set2
print("the symmeteric diifference of set1 and set2 is:", set1 ^ set2) #returns symmeteric difference which is (set1 | set2) - (set1 & set2)

