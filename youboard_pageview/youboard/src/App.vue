<template>
  <v-app>
    <v-layout column wrap>
      <v-layout v-if="window.width < 960" column wrap>
        <v-layout row wrap align-center justify-center class="mt-3 pl-3 pr-3">
          <v-flex xs1 md1>
            <v-icon large color="black">fas fa-share-alt</v-icon>
          </v-flex>
          <v-spacer></v-spacer>
            <v-img src="https://github.com/Deocksoo/my-first-blog/blob/master/blog/templates/blog/logo.png?raw=true" :width="window.width*0.3"></v-img>
          <v-spacer></v-spacer>
          <v-flex xs1>
            <v-icon large color="black">fas fa-search</v-icon>
          </v-flex>
        </v-layout>
        <v-layout row justify-space-between class='pl-2 pr-2 mt-1 mb-1'>
          <v-flex xs4 class="mr-1 ml-1">
            <v-btn block>유튜버</v-btn>
          </v-flex>
          <v-flex xs4 class="mr-1 ml-1">
            <v-btn block>채널</v-btn>
          </v-flex>
          <v-flex xs4 class="mr-1 ml-1">
            <v-btn block>인기영상</v-btn>          
          </v-flex>
        </v-layout>
      </v-layout>
      <v-layout v-else row wrap align-center class="mt-3 pl-3 pr-3">
        <v-flex sm2>
          <v-img src="https://github.com/Deocksoo/my-first-blog/blob/master/blog/templates/blog/logo.png?raw=true" alt=""></v-img>
        </v-flex>
        <v-flex md2 lg1 class="mr-1 ml-1">
          <v-btn block>유튜버</v-btn>
        </v-flex>
        <v-flex md2 lg1 class="mr-1 ml-1">
          <v-btn block>채널</v-btn>
        </v-flex>
        <v-flex md2 lg1 class="mr-1 ml-1">
          <v-btn block>인기영상</v-btn>          
        </v-flex>
        <v-spacer></v-spacer>
        <v-flex md1>
          <v-icon large color="black">fas fa-search</v-icon>
        </v-flex>
      </v-layout>
      <main-chart :window="window"></main-chart>
    </v-layout>
  </v-app>
</template>

<script>
import MainChart from './components/MainChart'
import PopularChart from './components/PopularChart'

export default {
  name: 'App',
  components: {
    MainChart,
    PopularChart
  },
  data () {
    return {
      window: {
        width: 0,
        height: 0
      }      
    }
  },
  created() {
    window.addEventListener('resize', this.handleResize)
    this.handleResize();
  },
  destroyed() {
    window.removeEventListener('resize', this.handleResize)
  },
  methods: {
    handleResize() {
      this.window.width = window.innerWidth;
      this.window.height = window.innerHeight;
    }
  }
}
</script>