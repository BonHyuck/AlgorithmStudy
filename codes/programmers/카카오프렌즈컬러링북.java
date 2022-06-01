package codes.programmers;


class Solution {
    int[] dr = {-1, 1, 0, 0};
    int[] dc = {0, 0, -1, 1};
    int cnt = 0;

    public void dfs(int r, int c, int[][] picture, int[][] visited){
        if(visited[r][c] == 1) {
            return;
        }
        
        visited[r][c] = 1;
        
        cnt++;
        
        for(int i =0; i < 4; i++){
            int new_r = r + dr[i];
            int new_c = c + dc[i];
            
            if(new_r < 0 || new_r >= picture.length || new_c < 0 || new_c >= picture[0].length) {
                continue;
            }
            
            if(picture[r][c] == picture[new_r][new_c] && visited[new_r][new_c] == 0){
                dfs(new_r, new_c, picture, visited);
            }            
        }        
    }


    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;

        int[][] visited = new int[m][n];
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(picture[i][j] != 0 && visited[i][j] == 0){
                    numberOfArea++;
                    dfs(i, j, picture, visited);
                }
                if(cnt > maxSizeOfOneArea) {
                    maxSizeOfOneArea = cnt;
                }

                cnt = 0;
            }
        }
        
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;

        return answer;
    }
}

public class 카카오프렌즈컬러링북{
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int cnt = 0;

    public static void dfs(int r, int c, int[][] picture, int[][] visited){
        if(visited[r][c] == 1) {
            return;
        }
        
        visited[r][c] = 1;
        
        cnt++;
        
        for(int i =0; i < 4; i++){
            int new_r = r + dr[i];
            int new_c = c + dc[i];
            
            if(new_r < 0 || new_r >= picture.length || new_c < 0 || new_c >= picture[0].length) {
                continue;
            }
            
            if(picture[r][c] == picture[new_r][new_c] && visited[new_r][new_c] == 0){
                dfs(new_r, new_c, picture, visited);
            }            
        }        
    }

    public static int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;

        int[][] visited = new int[m][n];
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(picture[i][j] != 0 && visited[i][j] == 0){
                    numberOfArea++;
                    dfs(i, j, picture, visited);
                }
                if(cnt > maxSizeOfOneArea) {
                    maxSizeOfOneArea = cnt;
                }

                cnt = 0;
            }
        }
        
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;

        return answer;
    }

    static int[][] arr = {{1, 1, 1, 0}, {1, 2, 2, 0}, {1, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 3}, {0, 0, 0, 3}};
    static int[] result = solution(6, 4, arr);

    public static void main(String[] args){
        for(int k = 0; k < result.length; k++){
            System.out.println(result[k]);
        }
    }
}