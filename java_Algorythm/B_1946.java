import java.util.*;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();
		for (int test_case = 1; test_case <= T; test_case++)
		{
			int supNum = sc.nextInt();
			
			// 배열생성
			int[][] arr = new int[supNum][2];
			for(int i=0;i<supNum;i++) {
				for(int j=0;j<2;j++) {
					arr[i][j] = sc.nextInt();
				}
			}

			// rank배열 생성 1로 초기화
			int[] rank = new int[supNum];
			for (int i = 0; i < rank.length; i++) {
				rank[i] = 1;
	        }
			
			// 점수 비교해서 낮은 행 rank++하기
			for(int i=0;i<arr.length;i++) {
				for(int j=0;j<arr.length;j++) {
					if(i!=j) {
						if(arr[i][0]>arr[j][0] && arr[i][1]>arr[j][1]) {
							rank[i]++;
						}
					}
				}
			}
			
			// rank 낮은 수 찾아서 인덱스 값 저장
			int max=rank[0];
			int index=0;
			for(int i=0;i<rank.length;i++) {
				if(rank[i] > max) {
					max = rank[i];
					index=i;
				}
			}
			
			// 최대값이 몇개인지?
			int count=0;
			for(int ran : rank) {
				if(max == ran) {
					count++;
				}
			}
			System.out.println(rank.length-count);
		}
	}
}
