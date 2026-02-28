import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const data = {

  AgeVsScreenTimeData: [
	['10-19', 5.5], 
	['20-29', 5.46], 
	['30-39', 5.58], 
	['40-49', 5.55], 
	['50-59', 0.0], 
	['60-69', 0.0], 
	['70-79', 0.0], 
	['80-89', 0.0]
],
	ScreenTimeVsHappiness: []

}

const getters = {
	AgeVsScreenTimeData: (state) => state.AgeVsScreenTimeData,
  ScreenTimeVsHappiness: (state) => state.ScreenTimeVsHappiness,
};


const actions = {

  	grabGraphData: ({ commit }) => {
      console.log('ACTION')
		// const path = 'http://localhost:5000/getInitialDataForGraphs';
		// axios.get(path)
		// 	.then((res) => {
		// 		commit('setHeatMapCauseLocationData', res.data['Heat_Map_Data'])
		// 	})
		// 	.catch((error) => {
		// 		console.log(error);
		// 	});
	},
};

const mutations = {
};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};