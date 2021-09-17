import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));		
		int N = Integer.parseInt(br.readLine());
		HashSet<String> arr = new HashSet<String>();  //중복제거를 위해 HashSet사용

		for (int i = 0; i < N; i++) {
			String tmp = br.readLine();
			arr.add(tmp);
		}
		
		ArrayList<String> list = new ArrayList<String>(arr);  //sort하기위해 다시 ArrayList로 변경
		Collections.sort(list, new Comparator<String>() {
			public int compare(String s1, String s2) {
				if (s1.length() == s2.length()) {
					return s1.compareTo(s2);
				}
				else {
					return Integer.compare(s1.length(), s2.length());
				}
			}
		});
		
		for (String s : list) {
			System.out.println(s);
		}
		
	}
}
