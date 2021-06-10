<template>
  <div class="container">
    <div class="row">
      <p class="mt-3 fw-bold" style="font-size: x-large;">MBTI Movies Recommendations</p>
      <p>원하는 MBTI 유형을 아래의 칸에서 선택해주세요</p>
      <p>※ JSON을 별도로 수집한 관계로 아직 좋아요와 리뷰 기능이 없는 오로지 추천에 충실한 코너입니다</p>
      <p>※ 개발자에 의해 임의적으로 선정된 데이터이기 때문에 신빙성은 다소 떨어질 수 있습니다</p>
      <div>
        <select class="form-select form-select-lg" name="mbti" id="mbti-select" v-model="mbti" @change="selectMbti">
          <option value="ALL">ALL</option>
          <option value="ESTJ">ESTJ</option>
          <option value="ISTJ">ISTJ</option>
          <option value="ESTP">ESTP</option>
          <option value="ISTP">ISTP</option>
          <option value="INFP">INFP</option>
          <option value="ENFP">ENFP</option>
          <option value="INFJ">INFJ</option>
          <option value="ENFJ">ENFJ</option>
          <option value="ESFP">ESFP</option>
          <option value="ISFP">ISFP</option>
          <option value="ENTJ">ENTJ</option>
          <option value="INTJ">INTJ</option>
          <option value="ISFJ">ISFJ</option>
          <option value="INTP">INTP</option>
          <option value="ENTP">ENTP</option>
          <option value="ESFJ">ESFJ</option>
        </select>
      </div>
    </div>
    <div class="row">
    <div v-if="select.ESTJ" class="col-6 title-font mx-0"> ESTJ #Action #Adventure <Mbtis :movies="estj_movies" /> </div>
    <div v-if="select.ESTP" class="col-6 title-font mx-0"> ESTP #RomCom #Action <Mbtis :movies="estp_movies" /> </div> 
    <div v-if="select.ISTJ" class="col-6 title-font mx-0"> ISTJ #Crime #Thriller <Mbtis :movies="istj_movies" /> </div>
    <div v-if="select.ISTP" class="col-6 title-font mx-0"> ISTP #Action #SF <Mbtis :movies="istp_movies" /> </div> 
    <div v-if="select.INFP" class="col-6 title-font mx-0"> INFP #Drama #Romance <Mbtis :movies="infp_movies" /> </div>
    <div v-if="select.ENFP" class="col-6 title-font mx-0"> ENFP #Romance #Animation <Mbtis :movies="enfp_movies" /> </div>
    <div v-if="select.INFJ" class="col-6 title-font mx-0"> INFJ #Animation #Family <Mbtis :movies="infj_movies" /> </div>
    <div v-if="select.ENFJ" class="col-6 title-font mx-0"> ENFJ #Romance #WhoDunIt <Mbtis :movies="enfj_movies" /> </div>
    <div v-if="select.ESFP" class="col-6 title-font mx-0"> ESFP #Romance #Action <Mbtis :movies="esfp_movies" /> </div> 
    <div v-if="select.ISFP" class="col-6 title-font mx-0"> ISFP #Thriller #Drama <Mbtis :movies="isfp_movies" /> </div>
    <div v-if="select.ENTJ" class="col-6 title-font mx-0"> ENTJ #Action #WhoDunIt <Mbtis :movies="entj_movies" /> </div> 
    <div v-if="select.INTJ" class="col-6 title-font mx-0"> INTJ #Crime #Thriller <Mbtis :movies="intj_movies" /> </div>
    <div v-if="select.ISFJ" class="col-6 title-font mx-0"> ISFJ #Family #Drama <Mbtis :movies="isfj_movies" /> </div>
    <div v-if="select.INTP" class="col-6 title-font mx-0"> INTP #Action #SF <Mbtis :movies="intp_movies" /> </div>
    <div v-if="select.ENTP" class="col-6 title-font mx-0"> ENTP #Thriller #WhoDunIt <Mbtis :movies="entp_movies" /> </div> 
    <div v-if="select.ESFJ" class="col-6 title-font mx-0"> ESFJ #Adventure #Action <Mbtis :movies="esfj_movies" /> </div>
    </div> 
  </div>
</template>

<script>
import axios from 'axios'
import Mbtis from '@/views/mbtis/Mbtis.vue'

export default {
  name: "Mbti",
  components: {
    Mbtis
  },
  data: function () {
    return {
      estj_movies : [],
      istj_movies : [],
      estp_movies : [],
      istp_movies : [],
      infp_movies : [],
      enfp_movies : [],
      infj_movies : [],
      enfj_movies : [],
      esfp_movies : [],
      isfp_movies : [],
      entj_movies : [],
      intj_movies : [],
      isfj_movies : [],
      intp_movies : [],
      entp_movies : [],
      esfj_movies : [],
      mbti: null,
      select: {
        ESTJ: true,
        ESTP: true,
        ISTJ: true,
        ISTP: true,
        INFP: true,
        ENFP: true,
        INFJ: true,
        ENFJ: true,
        ESFP: true,
        ISFP: true,
        ENTJ: true,
        INTJ: true,
        ISFJ: true,
        INTP: true,
        ENTP: true,
        ESFJ: true,
      }
      // 16개 유형 빈 리스트값 data 초기값 설정
    }
  },
  methods: {
    getMbti: function () {
      axios({
        method: 'get',
        url: `https://ssafypedia.link/movies/mbti/`,
      })
      .then((res) => {
        this.estj_movies = res.data[0]
        this.istj_movies = res.data[1]
        this.estp_movies = res.data[2]
        this.istp_movies = res.data[3]
        this.infp_movies = res.data[4]
        this.enfp_movies = res.data[5]
        this.infj_movies = res.data[6]
        this.enfj_movies = res.data[7]
        this.esfp_movies = res.data[8]
        this.isfp_movies = res.data[9]
        this.entj_movies = res.data[10]
        this.intj_movies = res.data[11]
        this.isfj_movies = res.data[12]
        this.intp_movies = res.data[13]
        this.entp_movies = res.data[14]
        this.esfj_movies = res.data[15]
      })
      .catch( (err) => {
          console.log(err)
      })
    },
    resetMbti: function() {
      for ( var selectmbti in this.select) {
        this.select[selectmbti] = true
      }
    },
    selectMbti: function () {
      for ( var selectmbti in this.select) {
        if (this.mbti !== selectmbti && this.mbti !== 'ALL') {
          this.select[selectmbti] = false
        } else if (this.mbti === 'ALL'){
          this.resetMbti()
        } else {
          this.select[selectmbti] = true
        }
      }
    },
  },
  created: function () {
    this.getMbti()
    this.resetMbti()
    // 생성되지마자 실행되도록 created에 함수 넣기
  },
}
</script>