import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
    credentials: {
      username: null,
      password: null,
    },
    credentials_pass: {
      // id: null,
      username: null,
      password: null,
      passwordConfirmation: null,
    },
    isLogin: false,
    isLight: true,
    isDark: false,
  },
  mutations: {
    GET_MOVIES: function (state) {
      // const MOVIE_URL = "http://api.themoviedb.org/3/movie/popular?api_key=7907fcdfc5896826871ad2a28bde5ab7&language=ko-kr&page=3";
      const MOVIE_URL = 'http://127.0.0.1:8000/movies/recommend/'
      axios.get(MOVIE_URL)
      .then((response) => {
        // console.log(response.data);
        state.movies = response.data;
      });
    },
    LOGIN: function (state) {
      state.isLogin = true
    },
    LOGOUT: function (state, isLogin) {
      state.isLogin = isLogin
    },
    SET_DARK: function (state) {
      if (state.isDark) {
        state.isDark = false
        state.isLight = true
      } else {
        state.isDark = true
        state.isLight = false
      }
    }
  },

  actions: {
    getMovies: function ({ commit }) {
      commit('GET_MOVIES')
    },
    login: function ({ commit }) {
      commit('LOGIN')
    },
    signup: function ({ commit }) {
      commit('SIGNUP')
    },
    logout: function ({ commit }, isLogin) {
      commit('LOGOUT', isLogin)
    },
    setDark: function ({ commit }) {
      commit('SET_DARK')
    }
  },
  getters: {
    // isLogin: function (state) {
    //   return state.isLogin
    // }
    isDark: function (state) {
      return state.isDark
    },
    isLight: function (state) {
      return state.isLight
    }
  },
  modules: {
  }
})