import Vue from 'vue'
import VueRouter from 'vue-router'
import Movie from '@/views/movies/Movie.vue'
import Genre from '@/views/movies/Genre.vue'
import Movies from '@/views/movies/Movies.vue'
import MovieList from '@/views/movies/MovieList.vue'
import MovieDetail from '@/views/movies/MovieDetail.vue'
import ReviewList from '@/views/movies/ReviewList.vue'
import Review from '@/views/movies/Review.vue'
import ReviewDetail from '@/views/movies/ReviewDetail.vue'
import CreateReview from '@/views/movies/CreateReview.vue'
import CreateComment from '@/views/movies/CreateComment.vue'
import Login from '@/views/accounts/Login.vue'
import Signup from '@/views/accounts/Signup.vue'
import Profile from '@/views/accounts/Profile.vue'
import MyProfile from '@/views/accounts/MyProfile.vue'
import MyComments from '@/views/accounts/MyComments.vue'
import MyCommentList from '@/views/accounts/MyCommentList.vue'
import Mbti from '@/views/mbtis/Mbti.vue'
import Mbtis from '@/views/mbtis/Mbtis.vue'
import MbtiList from '@/views/mbtis/MbtiList.vue'
import MbtiDetail from '@/views/mbtis/MbtiDetail.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/mbtis/recommend',
    name: 'Mbti',
    component: Mbti
  },
  {
    path: '/mbtis',
    name: 'Mbtis',
    component: Mbtis
  },
  {
    path: '/mbtis/mbtilist',
    name: 'MbtiList',
    component: MbtiList
  },
  {
    path: '/mbtis/mbtidetail',
    name: 'MbtiDetail',
    component: MbtiDetail
  },
  {
    path: '/movies/recommend',
    name: 'Movie',
    component: Movie
  },
  {
    path: '/movies/genre',
    name: 'Genre',
    component: Genre
  },
  {
    path: '/movies',
    name: 'Movies',
    component: Movies
  },
  {
    path: '/movies/list',
    name: 'MovieList',
    component: MovieList
  },
  {
    path: '/movies/detail',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/movies/reviewlist',
    name: 'ReviewList',
    component: ReviewList
  },
  {
    path: '/movies/review',
    name: 'Review',
    component: Review
  },
  {
    path: '/movies/reviewdetail',
    name: 'ReviewDetail',
    component: ReviewDetail
  },
  {
    path: '/movies/createreview',
    name: 'CreateReview',
    component: CreateReview
  },
  {
    path: '/movies/review/comment',
    name: 'CreateComment',
    component: CreateComment
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/accounts/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/accounts/myprofile',
    name: 'MyProfile',
    component: MyProfile
  },
  {
    path: '/accounts/mycomments',
    name: 'MyComments',
    component: MyComments
  },
  {
    path: '/accounts/mycommentlist',
    name: 'MyCommentList',
    component: MyCommentList
  },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
