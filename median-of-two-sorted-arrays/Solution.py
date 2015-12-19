class Solution(object):
	def findK(self, nums1, start1, len1, nums2, start2, len2, kth):
		if len1 <= 0:
			return nums2[start2 + kth - 1];
		if len2 <= 0:
			return nums1[start1 + kth - 1];

		if kth == 1:
			return min(nums1[start1], nums2[start2]);
		return 1.0;

	def findMedianSortedArrays(self, num1, num2):
		total = len(num1) + len(num2);
		if total & 0x01:
			return self.findK(num1, 0, len(num1), num2, 0, len(num2), (total + 1) // 2);
		else:
			return (self.findK(num1, 0, len(num1), num2, 0, len(num2), total // 2) + self.findK(num1, 0, len(num1), num2, 0, len(num2), total // 2 + 1))/ 2.0;


	def test(self):
		print 'hello'
