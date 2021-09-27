// 백준 11004번: K번째 수 (Silver 5)
// 일반적인 QuickSort가 아닌 pivot을 가운데 수로 정함으로써 NlogN에 정렬되도록 했다.

import java.io.*;
import java.util.*;
public class hw4_QuickSort {
	static int N, K;
	public static void main(String[] args) throws IOException {
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));		
		
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		int[] arr = new int[N];
		
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			int num = Integer.parseInt(st.nextToken());
			arr[i] = num;
		}
		
		quicksort(arr, 0, N-1);
		System.out.println(arr[K-1]);
		
	}
	public static void quicksort(int[] array, int left, int right) { 
		if (left >= right) { 
			return; 
		} 
		
		int pivot = partition(array, left, right);
		quicksort(array, left, pivot - 1);
		quicksort(array, pivot, right);
	}
	
	public static int partition(int[] array, int left, int right) {
		int mid = (left + right) / 2;
		int pivot = array[mid];
		 
		while (left <= right) {
			while (pivot < array[right]) {
				right--;
			}
			while (pivot > array[left]) {
				left++;
		    }
			if (left <= right) {
				swap(array, left, right);
				right--;
				left++;
			}
		}
		return left;
	}
	
	public static void swap(int[] array, int a, int b) {
	    int temp = array[a];
	    array[a] = array[b];
	    array[b] = temp;
	}

}
