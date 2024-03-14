#!/usr/bin/env python
# coding: utf-8

# In[36]:


graph={
    'start':['A','B'],
    'A':['Start','E','F'],
    'B':['Start','D','C'],
    'C':['B'],
    'D':['B','Goal'],
    'E':['B','G'],
    'F':['B'],
    'G':['E'],
    'Goal':['E','F']
}


# In[37]:


graph


# HANDLING QUEUE IN PYTHON:
# operations:
#  1.enqueue 
#  2.dequeue
#  3.size
#  4.front
#  5.rear

# In[5]:


from collections import deque


# In[6]:


Q=deque(["a","b","c","d","e"])


# In[7]:


Q.appendleft("0")


# In[8]:


Q


# In[9]:


Q.append("f")


# In[10]:


Q


# In[11]:


Q.popleft()


# In[12]:


Q.pop()


# In[13]:


Q


# In[14]:


Q[0]


# In[15]:


Q[-1]


# In[16]:


len(Q)


# In[16]:


graph={
    'Start':['A','B'],
    'A':['Start','E','F'],
    'B':['Start','D','C'],
    'C':['B'],
    'D':['B','Goal'],
    'E':['B','G'],
    'F':['B'],
    'G':['E'],
    'Goal':['E','F']
}


# In[17]:


from collections import deque 
def bfs(graph,Start,Goal):
    visited=[]
    queue=deque([Start])
    while queue:
        node=queue.popleft()
        if node not in visited:
            visited.append(node)
            print("I have visited:",node)
            neighbours=graph[node]
            if node==Goal:
                return("I have reached the goal,this is my traversal")
            for neighbour in neighbours:
                queue.append(neighbour)


# In[18]:


bfs(graph,"Start","Goal")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




