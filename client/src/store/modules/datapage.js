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

}

const getters = {
	AgeVsScreenTimeData: (state) => state.AgeVsScreenTimeData,
};


const actions = {
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