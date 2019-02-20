<template>
  <v-app>
    <v-layout column>
      <v-flex>
      <v-layout v-if="window.width < 960" column wrap>
        <v-layout row wrap align-center justify-center class="mt-3 pl-3 pr-3">
          <v-flex xs1 md1>
            <v-icon large color="black">fas fa-share-alt</v-icon>
          </v-flex>
          <v-spacer></v-spacer>
          <v-flex shrink>
            <v-img src="https://github.com/Deocksoo/my-first-blog/blob/master/blog/templates/blog/logo.png?raw=true" :width="window.width*0.4"></v-img>
          </v-flex>
          <v-spacer></v-spacer>
          <v-flex xs1>
            <v-icon large color="black">fas fa-search</v-icon>
          </v-flex>
        </v-layout>
        <v-layout row justify-space-between class='pl-2 pr-2 mt-1 mb-1'>
          <v-flex xs4 v-for="(item, index) in classification" :key="index" class="mr-1 ml-1">
            <v-btn block :color="item.criteria === activated ? '#F42072' : '#A9A9A9'" @click="view=item.chart; activated=item.criteria;">
              <strong style="color: white; font-size: 4.3vw;">{{ item.criteria }}</strong>
            </v-btn>
          </v-flex>
        </v-layout>
      </v-layout>
      <v-layout v-else row wrap align-center class="mt-3 pl-3 pr-3">
        <v-flex shrink>
          <v-img src="https://github.com/Deocksoo/my-first-blog/blob/master/blog/templates/blog/logo.png?raw=true" :width="window.width*0.2"></v-img>
        </v-flex>
        <v-flex md1 lg1 v-for="(item, index) in classification" :key="index" class="mr-1 ml-1">
          <v-btn block :color="item.criteria === activated ? '#F42072' : '#A9A9A9'" @click="view=item.chart; activated=item.criteria;">
            <strong style="color: white; font-size: 1.5vw;">{{ item.criteria }}</strong>
            </v-btn>
        </v-flex>
        <v-spacer></v-spacer>
        <v-flex md1>
          <v-icon large color="black">fas fa-search</v-icon>
        </v-flex>
      </v-layout>
      </v-flex>
      <v-flex>
        <component :is="view" :window="window" :rankData="getRankData"></component>
      </v-flex>
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
      },
      classification: [
        {
          criteria: "유투버",
          chart: "MainChart",
          dataKey: "Youtuber"
        },
        {
          criteria: "채널",
          chart: "MainChart",
          dataKey: "Channel"
        },
        {
          criteria: "인기영상",
          chart: "PopularChart",
          dataKey: "PopularVideo"
        }
      ],
      activated: "채널",
      view: "",
      rankData: {
        channelData: {},
        youtuberData: {},
        popularData: {}
      }
    }
  },
  created() {
    window.addEventListener('resize', this.handleResize)
    this.handleResize();
  },
  mounted() {
    this.$http.get('http://127.0.0.1:5000/channel').then((result) => {
      this.rankData.channelData = result.data
      this.view = "MainChart"
    })
  },
  destroyed() {
    window.removeEventListener('resize', this.handleResize)
  },
  methods: {
    handleResize() {
      this.window.width = window.innerWidth;
      this.window.height = window.innerHeight;
    }
  },
  computed: {
    getRankData() {
      if (this.activated == '채널') {
        return this.rankData.channelData;
      }
      else if (this.activated == '유투버') {
        return this.rankData.youtuberData;
      }
      else if (this.activated == '인기영상') {
        return this.rankData.popularData;
      }
    }
  },
}
</script>