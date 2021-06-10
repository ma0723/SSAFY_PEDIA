<template>
  <div class="container">
    <div class="row mx-3 my-5">
      <div class="col d-flex align-items-center justify-content-center">
        <!-- 상세 영화 이미지 -->
        <img :src="'https://image.tmdb.org/t/p/w500/' + movie.poster_path" alt="" style="width:350px">
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
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "MbtiDetail",
  data: function () {
    return {
      movie: this.$route.query.movie,
      rating: 0,
      day: null,
    }
  },
  components: {
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
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
  },
  created: function () {
    this.ratingToInt()
    this.dateToday()
  },
}
</script>

<style>

</style>