<template>
  <div>
    <!-- 댓글 배치 조절 필요 글라이더? -->
    <ul>
      <MyCommentList
        v-for="(comment, idx) in comments" 
        :key="idx"
        :comment="comment"
      />
    </ul>
  </div>
</template>

<script>
import MyCommentList from '@/views/accounts/MyCommentList.vue'

export default {
  name: "MyComments",
  components: {
    MyCommentList,
  },
  props: {
    comments: {
      type: Array,
    }
  },
}
</script>

<style>

</style>