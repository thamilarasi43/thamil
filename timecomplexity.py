def ArrayTwoCandidates(A,arr_size,sum):
 quickSort(A,0,arr_size-1)
 l=0
 r=ar_size-1
 while l<r:
  if(A[l]+A[r]==sum:
    return 1
  elif(a[l]+a[r]<sum:
   l+=1
  else:
   r-=1
 return 0  
