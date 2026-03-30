class Solution {
    /**
     * @param {number[][]} intervals
     * @param {number[]} newInterval
     * @return {number[][]}
     */
    insert(intervals, newInterval) {
        let res = [];

        for (let i = 0; i < intervals.length; i++) {
            // If newInterval ends before the current interval starts
            if (newInterval[1] < intervals[i][0]) {
                res.push(newInterval);
                return res.concat(intervals.slice(i));
            }
            // If newInterval overlaps with the current interval
            else if (newInterval[0] <= intervals[i][1]) {
                newInterval = [
                    Math.min(newInterval[0], intervals[i][0]),
                    Math.max(newInterval[1], intervals[i][1])
                ];
            } else {
                // If newInterval doesn't overlap, just push the current interval
                res.push(intervals[i]);
            }
        }

        // Add the final merged newInterval if it hasn't been added yet
        res.push(newInterval);
        return res;
    }
}
