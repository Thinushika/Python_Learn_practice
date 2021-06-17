#gradde 0 - 100
# less than 40 -- fail

#sam
#difference between the grade and the next multiple of 5 less than 3,
#round grade up to the next multiple of 5

Scanner sc = new Scanner(System.in);                 
int n = sc.nextInt();                 
int count = n;       
for (int i = 0; i < n; i++)        
{                  
for (int j = 1; j <= i*4; j++)            
{                
System.out.print(" ");            
}                        
for (int j = 1; j <= count; j++)                      
{                
System.out.print(j+" ");            
}                                     
for (int j = count-1; j >= 1; j--)            
{                               
System.out.print(j+" ");                        
}                         
System.out.println();                        
count--;      
}    
}}


for(i=0;i<10;++i)
  {
 
   printf("\n");
 
   for(j=0;j<=i;++j)
 
   {
     if(j==0 || i==j)
 
      a[i][j]=1;
 
      else
 
       a[i][j]=a[i-1][j-1]+a[i-1][j];
 
       printf("%4d",a[i][j]);
   }
  }
}
String s = "";
int spc = 0;
for (int i = 4; i >= 0; i++) {
    String line = "";
    for (int sp = 0; sp < spc; sp++) { 
       line += " ";   
} 
   line += Math.pow(11, i) + "\n";
    s = line + s;
    spc++;}print(s);



    void main()
{
int a[10][10],i,j;
for(i=0;i<10;++i)
  {

   printf("\n");
   for(j=0;j<=i;++j)
   {
     if(j==0 || i==j)
      a[i][j]=1;
      else
       a[i][j]=a[i-1][j-1]+a[i-1][j];
       printf("%4d",a[i][j]);

   }
  }



}