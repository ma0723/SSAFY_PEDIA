<template>
  <div class="container">
    <div class="row mx-3 my-5">

      <div class="col d-flex align-items-center justify-content-center">
        <!-- 상세 영화 이미지 -->
        <img :src="'https://image.tmdb.org/t/p/w500/' + movie.poster_path" alt="" style="width:400px">
        <!-- 이미지 사이즈 조절 필요 -->
      </div>

      <div class="col">
        <!-- 상세 영화 조회 -->
        <p class="content-font"> Title <span>{{ movie.title }}</span></p>
        <div class="content-font">
          <p> Genre {{movie.genre}}</p>
          <p> Release Date {{day}}</p> 
          <!-- 연월시만 가져오는 변수로 함수 실행 후 변수값 대입 -->
          <p> 
            Rating {{movie.vote_average}} 
            <span v-for="(i, idx) in rating" :key="idx">
              <!-- 평점의 정수만큼 별의 개수 표시 -->
              <i style="color:yellow;" class="fas fa-star"></i>
            </span> 
          </p>
        </div>
        <div class="mini-font"> 
          <p class="content-font"> Overview </p>
          <span> {{ movie.overview }}</span>
        </div>

        <div>
        <!-- 좋아요 -->
          <i id="heart" v-if="isLiking" @click="like" style="color:crimson; font-size:30px; text-align:center; margin-top:30px;" class="fas fa-heart"></i>
          <i id="heart" v-else @click="like" style="font-size:30px; text-align:center; margin-top:30px;" class="far fa-heart"></i>
          <p class="st-font" style="text-align:center; margin-top:5px; font-weight: bold; font-size: small;">LIKE {{ numLike }}개</p>
        </div>

        <div>
        <!-- 리뷰 작성 -->
          <CreateReview :movie="movie" @create-review="createReview"/>
        </div>

      </div>
    </div>
    
    <div class="row mx-3 my-5">
    <!-- 상세 영화 전체 리뷰 조회 -->
      <div v-if="reviews">
        <ReviewList :reviews="reviews"/>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"
import ReviewList from '@/views/movies/ReviewList.vue'
import CreateReview from '@/views/movies/CreateReview.vue'

export default {
  name: "MovieDetail",
  data: function () {
    return {
      movie: this.$route.query.movie,
      numLike: 0,
      liking: '',
      reviews: null,
      me: null,
      rating: 0,
      day: null,
    }
  },
  components: {
    ReviewList,
    CreateReview,
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getUser: function () {
      const config = this.setToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post(`https://ssafypedia.link/accounts/profile/`, info, config)
      .then((res) => {
        this.me = res.data
        if (this.me.like_movies.includes(this.movie.id)) {
          this.liking = true
        } else {
          this.liking = false
        }
      })
      .catch((err) => {
        console.log(err)
      })
    },
    like: function () {
      axios({
        method: 'post',
        url: `https://ssafypedia.link/movies/${this.me.id}/${this.movie.id}/like/`,
        headers: this.setToken()
      })
      .then((res) => {
        this.numLike = res.data.count
        this.liking = res.data.liked
      })
      .catch((err) => {
        console.log(err)
      })
    },
    number: function () {
      this.numLike = this.movie.like_user.length
    },
    ratingToInt: function () {
      this.rating = Math.floor(Number(this.movie.vote_average))
      // str을 숫자로 변환 후 Number() 
      // 내림 함수 Math.floor()
    },
    dateToday: function() {
      this.day = String(this.movie.release_date).substring(0, 10)
      // 개봉 일시에서 시분초 제외 연월일
      // 문자열 변환 후 String()
      // 자르기 .substring(index)
    },
    getReviews: function () {
      axios({
        method: 'get',
        url: `https://ssafypedia.link/movies/${this.movie.id}/review/`,
        headers: this.setToken()
      })
      .then((res) => {
        this.reviews = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    createReview: function () {
      this.reviews = []
      this.getReviews()
    }
  },
  computed: {
    isLiking: function () {
      return this.liking
    },
  },
  created: function () {
    this.number()
    this.getUser()
    this.ratingToInt()
    this.dateToday()
    this.getReviews()
  },
}
</script>

<style>

</style>