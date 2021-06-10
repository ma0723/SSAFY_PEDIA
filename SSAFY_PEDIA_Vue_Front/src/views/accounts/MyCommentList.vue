<template>
  <div class="container">
    <div class="col d-flex align-items-start mt-2">
      {{comment.content}}
      {{createDay}}
      {{createTime}}
      <button type="button" class="btn btn-sm mx-2" @click="reviewDetail" :class="{ 'btn-outline-dark': isLight, 'btn-outline-light': isDark }">REVIEW DETAIL</button>
      <button type="button" class="btn btn-sm mx-2" @click="movieDetail" :class="{ 'btn-outline-dark': isLight, 'btn-outline-light': isDark }">MOVIE DETAIL</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "MyCommentList",
  props: {
    comment: {
      type: Object,
      required: true
    },
  },
  data: function () {
    return {
      review: null,
      movie: null,
      createDay: null,
      createTime: null,
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    commentReview: function () {
      axios({
        method: 'get',
        url: `https://ssafypedia.link/movies/review/${Number(this.comment.review)}/`,
        // 리뷰 pk는 정수형 입력 Number()
        headers: this.setToken()
      })
      .then((res) => {
        console.log(res)
        this.review = res.data
        axios({
          method: 'get',
          url: `https://ssafypedia.link/movies/${Number(this.review.movie)}/`,
          // 영화 pk는 정수형 입력 Number()
          headers: this.setToken()
        })
        .then((res) => {
          console.log(res)
          this.movie = res.data
        })
        .catch((err) => {
          console.log(err)
        })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    reviewDetail: function () {
      this.$router.push({ name: 'ReviewDetail', query: { review: this.review, movie: this.movie } })
    },
    movieDetail: function () {
      this.$router.push({ name: 'MovieDetail', query: { movie: this.movie } })
    },
    createDate: function() {
      const day = String(this.comment.created_at).substring(0, 10)
      const time = String(this.comment.created_at).substring(11, 19)
      this.createDay = day 
      this.createTime = time
      // 개봉 일시에서 시분초 제외 연월일
      // 문자열 변환 후 String()
      // 자르기 .substring(index)
    },
  },
  created: function () {
    this.commentReview()
    this.createDate()
  },
  computed: {
    isDark: function () {
      return this.$store.getters.isDark
    },
    isLight: function () {
      return this.$store.getters.isLight
    },
  },
}
</script>

<style>

</style>