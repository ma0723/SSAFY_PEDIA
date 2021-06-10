<template>
  <div class="container">
    <div class="row mx-3 my-5" >    
    <!-- 영화 이미지 및 상세 리뷰 조회 -->

      <div class="col d-flex align-items-center justify-content-center">
      <!-- 영화 이미지 -->
        <img style="width: 330px" :src="'https://image.tmdb.org/t/p/w500/' + movie.poster_path" alt="">
        <!-- 이미지 사이즈 수정 필요 -->
      </div>

      <div class="col">
        <!-- 상세 리뷰 조회 -->
        <p class="content-font mousecursor" @click="reviewProfile"> Reviewer {{ review.userName }}</p>
        <p class="content-font mousecursor" @click="movieDetail"> Movie Title {{ review.movie_title }}</p>
        <p class="content-font"> Title {{ review.title }}</p>
        <p class="content-font"> Rating   
          {{ review.rank }}      
          <span v-for="(i, idx) in rating" :key="idx">
            <i style="color:yellow;" class="fas fa-star"></i>
          </span> 
        </p>
        <p class="content-font"> Content </p>
        <p class="mini-font"> {{ review.content }} </p>
        <p class="content-font"> Created_at {{ createDay }} {{ createTime }}</p>
        <p class="content-font"> Updated_at {{ updateDay }} {{ updateTime }}</p>
        <!-- 날짜 연원일 시분까지만 슬라이싱 필요 -->

        <!-- 상세 리뷰 삭제 수정 -->
        <div class="container mt-2" v-if="updateseen">
          <div class="row my-2">
            <input type="text" v-model="title" :placeholder="review.title">
          </div>
          <div class="row my-2">
            <input type="text" v-model="rank" :placeholder="review.rank">
          </div>
          <div class="row my-2">
            <textarea rows="4" v-model="content" :placeholder="review.content">
            </textarea>
          </div>
        </div>

        <!-- 상세 리뷰 삭제 수정 버튼 -->
        <div class="row px-0 mt-3">
          <!-- 버튼 배치 조절 필요 -->
          <div v-if="buttonseen" class="row px-0 mb-3 mx-2">
            <button type="button" class="btn btn-outline-primary" @click="update">Review Update</button>
            <!-- 리뷰 수정 신청 버튼 -->
          </div>
          <div v-if="updateseen" class="row px-0 mb-3 mx-2">
            <button type="button" class="btn btn-outline-primary" @click="updateReview">Review Update</button>
            <!-- 리뷰 수정 완료 버튼 -->
          </div>
          <div v-if="updateseen" class="row px-0 mb-3 mx-2">
            <button type="button" class="btn" @click="cancelUpdate" :class="{ 'btn-outline-dark': isLight, 'btn-outline-light': isDark }">Cancel</button>
            <!-- 리뷰 수정 취소 버튼 -->
          </div>
          <div class="row px-0 mx-2">
            <button type="button" class="btn btn-outline-danger" @click="deleteReview">Review Delete</button>
            <!-- 리뷰 삭제 버튼 -->
          </div>
        </div>

        <!-- 댓글 생성 -->
        <div class="row px-0 mt-3">
          <CreateComment :review="review" @create-comment="getComments"/>
        </div>
      
      </div>
    </div>

    <div class="row mx-3 my-5">
    <!-- 댓글창 -->
      <ul v-if="comments">
        <li v-for="(comment, idx) in comments" :key="idx" style="list-style-type: none;" class="mb-2">
        <!-- li tag 점 제거(list-style-type: none;) -->
          <!-- 댓글 조회 -->
          <span @click="commentProfile(comment)" class="mousecursor fw-bold"> {{ comment.userName }} </span>
          <span> {{ comment.content }} </span>
          <!-- 댓글 작성 시간 슬라이싱 -->

          <!-- 댓글 삭제 -->
          <button type="button" class="btn btn-sm" @click="deleteComment(comment)" :class="{ 'btn-outline-dark': isLight, 'btn-outline-light': isDark }">Comment Delete</button>
        </li>
      </ul>
    </div>

  </div>
</template>

<script>
import CreateComment from '@/views/movies/CreateComment.vue'
import axios from 'axios'

export default {
  name: "ReviewDetail",
  components: {
    CreateComment,
  },
  data: function () {
    return {
      review: this.$route.query.review,
      movie: this.$route.query.movie,
      comments: null,
      title: null,
      content: null,
      rank: null,
      updateseen: false,
      buttonseen: true,
      ranking: 0,
      createTime: null,
      createDay: null,
      updateTime: null,
      updateDay: null,
      commentTime: null,
      commentDay: null,
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
    getComments: function () {
      axios({
        method: 'get',
        url: `https://ssafypedia.link/movies/review/${this.review.id}/comments/`,
        headers: this.setToken()
      })
      .then((res) => {
        this.comments = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    updateReview: function () {
      const reviewItem = {
        title: this.title,
        content: this.content,
        rank: this.rank
      }
      if (reviewItem.content) {
        axios({
          method: 'put',
          url: `https://ssafypedia.link/movies/review/${this.review.id}/`,
          data: reviewItem,
          headers: this.setToken()
        })
        .then((res) => {
          console.log(res)
          axios({
              method: 'get',
              url: `https://ssafypedia.link/movies/review/${this.review.id}/`,
              headers: this.setToken()
            })
            .then((res) => {
              this.review = res.data
              this.ratingToInt()
              this.updateDate()
              this.updateseen = false
              this.buttonseen = true
            })
            .catch((err) => {
              console.log(err)
            })
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    update: function () {
      const reviewItem = {
        title: this.review.title,
        content: this.review.content,
        rank: this.review.rank
      }
      axios({
        method: 'put',
        url: `https://ssafypedia.link/movies/review/${this.review.id}/`,
        data: reviewItem,
        headers: this.setToken()
      })
      .then((res) => {
        this.updateseen = true
        this.buttonseen = false
        console.log(res)
      })
      .catch((err) => {
        this.updateseen = false
        this.buttonseen = true
        alert("본인이 작성한 글만 수정 가능합니다!")
        console.log(err)
      })
    },
    cancelUpdate: function () {
      this.updateseen = false
      this.buttonseen = true
    },
    deleteReview: function () {
      axios({
        method: 'delete',
        url: `https://ssafypedia.link/movies/review/${this.review.id}/`,
        headers: this.setToken()
      })
      .then((res) => {
        console.log(res)
        alert("리뷰가 삭제되었습니다!")
        this.$router.push({ name: 'MovieDetail', query: { movie: this.movie } })
      })
      .catch((err) => {
        console.log(err)
        alert("본인만 삭제가능합니다!")
      })
    },
    deleteComment: function (comment) {
      axios({
        method: 'delete',
        url: `https://ssafypedia.link/movies/review/${this.review.id}/comment/${comment.id}/`,
        headers: this.setToken()
      })
      .then((res) => {
        console.log(res)
        this.getComments()
        this.$router.push({ name: 'ReviewDetail', query: { movie: this.movie, review: this.review } })
        alert("댓글 삭제되었습니다!")
      })
      .catch((err) => {
        console.log(err)
        alert("본인만 삭제가능합니다!")
      })
    },
    reviewProfile: function () {
      this.$router.push({ name: "Profile" , query: { user: this.review.user, userName: this.review.userName } })
    },
    commentProfile: function (comment) {
      this.$router.push({ name: "Profile" , query: { user: Number(comment.user), userName: comment.userName } })
    },
    movieDetail: function () {
      this.$router.push({ name: "MovieDetail" , query: { movie: this.movie } })
    },
    ratingToInt: function () {
      this.rating = Math.floor(Number(this.review.rank))
    },
    createDate: function() {
      const day = String(this.review.created_at).substring(0, 10)
      const time = String(this.review.created_at).substring(11, 19)
      this.createDay = day 
      this.createTime = time
    },
    updateDate: function() {
      const day = String(this.review.updated_at).substring(0, 10)
      const time = String(this.review.updated_at).substring(11, 19)
      this.updateDay = day 
      this.updateTime = time
    },
  },
  created: function () {
    this.ratingToInt()
    this.getComments()
    this.createDate()
    this.updateDate()
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