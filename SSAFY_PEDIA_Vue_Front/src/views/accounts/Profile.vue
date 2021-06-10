<template>
  <div>
    <p class="title-font">{{user.username}} Profile</p>
    <div class="container">
      <p class="content-font">Likes Movies of {{user.username}}</p>
      <Movies :movies="myLikeMovies" />
      <p class="content-font">Reviews by {{user.username}}</p>
      <ReviewList :reviews="myReviews"/>
      <p class="content-font">Comments by {{user.username}}</p>
      <MyComments :comments="myComments"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"
import Movies from '@/views/movies/Movies.vue'
import ReviewList from '@/views/movies/ReviewList.vue'
import MyComments from '@/views/accounts/MyComments.vue'
// 하위 컴포넌트 import

export default {
  name: "MyProfile",
  components: {
    // 좋아요한 영화들 보여줄 리스트
    // 작성한 리뷰들 보여줄 리스트
    // 작성한 댓글들 보여줄 리스트
    Movies,
    ReviewList,
    MyComments,
  },
  data: function () {
    return {
      user_pk: this.$route.query.user,
      userName: this.$route.query.userName,
      user: [],
      myLikeMovies: [],
      myReviews: [],
      myComments: [],
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
    getMyName: function () {
      const config = this.setToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post(`https://ssafypedia.link/accounts/${this.user_pk}/profile/`, info, config)
      .then((res) => {
        this.user = res.data
        // user 본인을 대입한 Userserializer가 전송한 data
        
        const likeItem = this.user.like_movies
        // 내가 좋아요한 영화들 (pk list)
        axios.post(`https://ssafypedia.link/movies/${this.user.id}/likes/`, likeItem, config)
        .then( (res) => {
          this.myLikeMovies = res.data
        })
        .catch( (err) => {
          console.log(err)
        })

        const reviewItem = this.user.reviews
        // 내가 작성한 리뷰들 (pk list)
        axios.post(`https://ssafypedia.link/movies/${this.user.id}/reviews/`, reviewItem, config)
        .then( (res) => {
          this.myReviews = res.data
        })
        .catch( (err) => {
          console.log(err)
        })

        const commentItem = this.user.comments
        // 내가 작성한 리뷰들 (pk list)
        axios.post(`https://ssafypedia.link/movies/${this.user.id}/comments/`, commentItem, config)
        .then( (res) => {
          this.myComments = res.data
        })
        .catch( (err) => {
          console.log(err)
        })

      })
      .catch( (err) => {
          console.log(err)
      })
    },
  },
  created: function () {
    this.getMyName()
    // 생성되지마자 실행되도록 created에 함수 넣기
  },
}

</script>

<style>

</style>