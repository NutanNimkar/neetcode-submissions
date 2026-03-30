class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    canJump(nums) {

        let goal = nums.length - 1;
        
        for(let i = nums.length; i >= 0;  i--){
            if(i + nums[i] >= goal){
                goal = i
            }
        }
        if(goal === 0){
            return true
        }else{
            return false
        }
    }
}
