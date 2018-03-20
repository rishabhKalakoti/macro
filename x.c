#include<stdio.h>
#define ll long long
int main()
{
	// input
	ll N;
	scanf("%lli", &N);
	ll arr[N];
	for(ll i=0;i<N;i++)
		scanf("%lli", &arr[i]);
	ll edges[N-1][2];
	for(ll i=0;i<N-1;i++)
		scanf("%lli %lli", &edges[i][0], &edges[i][1]);
	ll count=0;
	for(ll i=0;i<N-1;i++)
	{
		ll a=0,b=0;
		ll visited[N]={0};
		ll flag=0;
		ll v;
		ll st[N];
		stPtr=-1;
		v=1;
		st[++stPtr]=v;
		while(stPtr >= 0)
		{
			v=st[stPtr--];
			visited[v-1] = 1;
			a = a | arr[v-1];
			for(ll j=0; j<N-1;j++)
			{
				if(i!=j)
				{
					if(edges[j][0]==v && visited[edges[j][1]-1]==0)
						st[++stPtr]=edges[j][1];
					else if(edges[j][1]==v && visited[edges[j][0]-1]==0)
						st[++stPtr]=edges[j][0];
				}
			}
		}
		v=1;
		while(visited[v-1]==1)
		{
			v++;
		}
		st[++stPtr]=v;
		while(stPtr >= 0)
		{
			v=st[stPtr--];
			visited[v-1] = 1;
			b = b | arr[v-1];
			for(ll j=0; j<N-1;j++)
			{
				if(i!=j)
				{
					if(edges[j][0]==v && visited[edges[j][1]-1]==0)
						st[++stPtr]=edges[j][1];
					else if(edges[j][1]==v && visited[edges[j][0]-1]==0)
						st[++stPtr]=edges[j][0];
				}
			}
		}
		if(a==b)
			count++;
	}
	printf("%lli\n",count);
	return 0;
}
