class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        Set<Integer> wins = new HashSet<>();
        Map<Integer, Integer> loses = new HashMap<>();
        
        for(int i=0; i<matches.length; i++){
            wins.add(matches[i][0]);
            loses.put(matches[i][1], loses.getOrDefault(matches[i][1], 0) + 1);
            
            if(loses.containsKey(matches[i][0])){
                wins.remove(matches[i][0]);
            }
            
            if(wins.contains(matches[i][1])){
                wins.remove(matches[i][1]);
            }
        }
        
        List<Integer> win_list = new ArrayList<>(wins);
        // 리스트 정렬 (작은 순서대로)
        win_list.sort(Integer::compareTo);
        
        List<Integer> lose_list = new ArrayList<>();
        for(Map.Entry<Integer, Integer> entry : loses.entrySet()){
            if(entry.getValue() == 1){
                lose_list.add(entry.getKey());
            }
        }
        lose_list.sort(Integer::compareTo);
        List<List<Integer>> result = new ArrayList<>();
        result.add(win_list);
        result.add(lose_list);
        
        return result;
    }
}