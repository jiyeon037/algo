import java.util.*;

public class Main {
	
	static int n, m;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		n = sc.nextInt(); // node 1~n
		m = sc.nextInt();
		
		List<List<Integer>> list = new ArrayList<List<Integer>>();
		
		int indegree[] = new int[n+1];
		
		for(int i=0; i<=n; i++)
			list.add(new ArrayList<Integer>());
	
		while(m --> -1){
			String str[] = sc.nextLine().split(" ");
			
			// 입력을 배열로 받을 것임으로,
			// 불필요한 맨 앞 사이즈 입력 무시 위해 i를 1부터 설정
			for(int i=2; i<str.length; i++) {
				int a = Integer.parseInt(str[i-1]);
				int b = Integer.parseInt(str[i]);
				
				list.get(a).add(b);				
				indegree[b]++;
			}
		}
		
		topologicalSort(indegree, list);
	}

	private static void topologicalSort(int[] indegree, List<List<Integer>> list) {
		
		Queue<Integer> Q = new LinkedList<>();
		List<Integer> result = new ArrayList<>();
		
		for(int i=1; i<=n; i++) {
			if(indegree[i] == 0) Q.offer(i);
		}
		
		while(!Q.isEmpty()) {
			int cur = Q.poll();
			result.add(cur);
			
			for(Integer i : list.get(cur)) {
				indegree[i]--;
				if(indegree[i] == 0) Q.offer(i);
			}
		}
		
		if(result.size() == n)
			for(int i=0; i<result.size(); i++)
				System.out.println(result.get(i));
		else
			System.out.println(0);
		
	}
}