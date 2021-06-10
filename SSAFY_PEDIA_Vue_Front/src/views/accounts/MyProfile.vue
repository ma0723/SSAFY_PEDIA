<template>
  <div>
    <p class="title-font">{{user.username}} Profile</p>
    <p> {{user.last_name}}{{user.first_name}}님 SSAFY PEDIA에 오신 것을 환영합니다</p>
    <!-- 본인 프로필인 경우에만 자신의 이름을 볼 수 있도록 설정 -->
    <!-- 타인 프로필로 검색한 경우 볼 수 없다 -->
    <div class="container">
      <p class="content-font"> HomePage Manual 
        <button type="button" class="btn btn-sm mx-1" @click="openManual" :class="{ 'btn-outline-dark': isLight, 'btn-outline-light': isDark }">DETAIL</button>
      </p>
        <div v-if="open" class="text-start my-3">
          <p> 영화 혹은 리뷰 카드를 누르면 상세 영화 혹은 리뷰 조회 페이지로 이동할 수 있습니다 </p>
          <span> 영화 추천 </span>
          <ul>
            <li> <span> Movies 약 160개의 인기 영화 중 개봉일 및 평점순으로 영화를 추천합니다 </span> </li>
            <li> <span> Genre Recommendation 약 160개의 인기 영화 중 장르별로 영화를 추천합니다 </span> </li>
            <li> <span> Mbti Recommendation 16개의 MBTI 유형마다 4개씩 총 64개의 영화를 추천합니다 </span> </li>
          </ul>
          <span> 상세 영화 조회 페이지 </span>
          <br>
          <ul>
            <li> <span> 상세 리뷰 조회 페이지에서 영화 제목, 개봉날짜, 평점, 줄거리 등이 간략히 기재되어 있습니다. </span> </li>
            <li> <span> 상세 영화 조회 페이지에서 좋아요 및 리뷰 작성이 가능합니다 (MBTI 추천 제외) </span> </li>
            <li> <span> 상세 리뷰 조회 페이지에서 리뷰 작성 및 해당 영화 전체 리뷰 조회가 가능합니다 (MBTI 추천 제외) </span> </li>
          </ul>
          <span> 상세 리뷰 조회 페이지 (MBTI 추천 제외) </span>
          <br>
          <ul>
            <li> <span> 상세 리뷰 조회 페이지에서 본인 리뷰 수정 및 삭제가 가능합니다 </span> </li>
            <li> <span> 상세 리뷰 조회 페이지에서 댓글 작성 및 본인 댓글 삭제가 가능합니다 </span> </li>
            <li> <span> 상세 리뷰 조회 페이지의 Movie Title을 클릭하면 해당 상세 영화 조회 페이지로 이동할 수 있습니다 </span> </li>
            <li> <span> 상세 리뷰 조회 페이지의 Reviewer 혹은 댓글 작성자를 클릭하면 해당 유저의 프로필로 이동할 수 있습니다 </span> </li>
          </ul>
        </div>
      <p class="content-font">Likes Movies of {{user.username}}</p>
      <div v-if="myLikeMovies">
        <Movies 
          v-if="myLikeMovies"
          :movies="myLikeMovies" 
        />
      </div>
      <p class="content-font">Reviews by {{user.username}}</p>
      <div v-if="myReviews">
        <ReviewList 
          v-if="myReviews"
          :reviews="myReviews"
        />
      </div>
      <p class="content-font">Comments by {{user.username}}</p>
      <div v-if="myComments">
        <MyComments 
          v-if="myComments"
          :comments="myComments"
        />
      </div>
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
      user: [],
      myLikeMovies: [],
      myReviews: [],
      myComments: [],
      open: false,
      // 홈페이지 메뉴얼 초기값
      seenMyMovies: false,
      seenReview: false,
      seenComment: false,
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
      axios.post(`https://ssafypedia.link/accounts/profile/`, info, config)
      .then((res) => {
        this.user = res.data
        // user 본인을 대입한 Userserializer가 전송한 data
        
        const likeItem = this.user.like_movies
        // 내가 좋아요한 영화들 (pk list)
        axios.post(`https://ssafypedia.link/movies/${this.user.id}/likes/`, likeItem, config)
        .then( (res) => {
          this.myLikeMovies = res.data
          if (this.myLikeMovies) {
            this.seenMyMovies = true
          } else {
            this.seenMyMovies = false
          }
        })
        .catch( (err) => {
          console.log(err)
        })

        const reviewItem = this.user.reviews
        // 내가 작성한 리뷰들 (pk list)
        axios.post(`https://ssafypedia.link/movies/${this.user.id}/reviews/`, reviewItem, config)
        .then( (res) => {
          this.myReviews = res.data
          if (this.myReviews) {
            this.seenReview = true
          } else {
            this.seenReview = false
          }
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
    openManual: function () {
      if (this.open === false) {
        this.open = true
      } else {
        this.open = false
      }
    },
  },
  created: function () {
    this.getMyName()
    // 생성되지마자 실행되도록 created에 함수 넣기
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