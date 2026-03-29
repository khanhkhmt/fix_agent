<template>
  <div class="sidebar">
    <div class="sidebar-logo" @click="goHome">
      <img src="@/assets/logo_oriagent.svg" alt="Oriagent" class="logo-img" />
    </div>
    
    <el-menu
      :default-active="activeMenu"
      class="sidebar-menu"
      @select="handleSelect"
      background-color="transparent"
      text-color="#3d4566"
      active-text-color="#000"
    >
      <el-menu-item index="/home">
        <i class="el-icon-monitor"></i>
        <span slot="title">{{ $t("header.smartManagement") }}</span>
      </el-menu-item>
      
      <el-submenu v-if="userInfo.superAdmin" index="models">
        <template slot="title">
          <i class="el-icon-cpu"></i>
          <span>{{ $t("header.modelConfig") }}</span>
        </template>
        <el-menu-item index="/model-config?tab=vad">
          <i class="el-icon-microphone"></i>
          <span>{{ $t("modelConfig.vad") }}</span>
        </el-menu-item>
        <el-menu-item index="/model-config?tab=asr">
          <i class="el-icon-chat-dot-round"></i>
          <span>{{ $t("modelConfig.asr") }}</span>
        </el-menu-item>
        <el-menu-item index="/model-config?tab=llm">
          <i class="el-icon-cpu"></i>
          <span>{{ $t("modelConfig.llm") }}</span>
        </el-menu-item>
        <el-menu-item index="/model-config?tab=vllm">
          <i class="el-icon-picture-outline"></i>
          <span>{{ $t("modelConfig.vllm") }}</span>
        </el-menu-item>
        <el-menu-item index="/model-config?tab=intent">
          <i class="el-icon-aim"></i>
          <span>{{ $t("modelConfig.intent") }}</span>
        </el-menu-item>
        <el-menu-item index="/model-config?tab=tts">
          <i class="el-icon-headset"></i>
          <span>{{ $t("modelConfig.tts") }}</span>
        </el-menu-item>
        <el-menu-item index="/model-config?tab=memory">
          <i class="el-icon-collection"></i>
          <span>{{ $t("modelConfig.memory") }}</span>
        </el-menu-item>
        <el-menu-item index="/model-config?tab=rag">
          <i class="el-icon-notebook-2"></i>
          <span>{{ $t("modelConfig.rag") }}</span>
        </el-menu-item>
      </el-submenu>
      
      <el-submenu index="more">

        <template slot="title">
          <i class="el-icon-more"></i>
          <span>{{ $t("header.paramDictionary") }}</span>
        </template>
        
        <el-menu-item v-if="featureStatus.voiceClone" index="/voice-clone-management">
          <i class="el-icon-mic"></i>
          <span>{{ $t("header.voiceCloneManagement") }}</span>
        </el-menu-item>
        
        <el-menu-item v-if="featureStatus.knowledgeBase" index="/knowledge-base-management">
          <i class="el-icon-notebook-1"></i>
          <span>{{ $t("header.knowledgeBase") }}</span>
        </el-menu-item>
        
        <template v-if="userInfo.superAdmin">
          <el-menu-item index="/user-management">
            <i class="el-icon-user"></i>
            <span>{{ $t("header.userManagement") }}</span>
          </el-menu-item>
          
          <el-menu-item index="/ota-management">
            <i class="el-icon-upload"></i>
            <span>{{ $t("header.otaManagement") }}</span>
          </el-menu-item>
          
          <el-menu-item index="/provider-management">
            <i class="el-icon-connection"></i>
            <span>{{ $t("header.providerManagement") }}</span>
          </el-menu-item>
          
          <el-menu-item index="/agent-template-management">
            <i class="el-icon-copy-document"></i>
            <span>{{ $t("header.agentTemplate") }}</span>
          </el-menu-item>
          
          <el-menu-item index="/params-management">
            <i class="el-icon-setting"></i>
            <span>{{ $t("header.paramManagement") }}</span>
          </el-menu-item>
          
          <el-menu-item index="/dict-management">
            <i class="el-icon-document"></i>
            <span>{{ $t("header.dictManagement") }}</span>
          </el-menu-item>
          
          <el-menu-item index="/server-side-management">
            <i class="el-icon-set-up"></i>
            <span>{{ $t("header.serverSideManagement") }}</span>
          </el-menu-item>
          
          <el-menu-item index="/feature-management">
            <i class="el-icon-magic-stick"></i>
            <span>{{ $t("header.featureManagement") }}</span>
          </el-menu-item>
        </template>
      </el-submenu>
    </el-menu>
    
    <div class="sidebar-footer">
      <version-footer />
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import VersionFooter from "./VersionFooter.vue";

export default {
  name: "SideBar",
  components: {
    VersionFooter
  },
  computed: {
    ...mapState({
      featureStatus: (state) => ({
        voiceClone: state.pubConfig.systemWebMenu?.features?.voiceClone?.enabled,
        knowledgeBase: state.pubConfig.systemWebMenu?.features?.knowledgeBase?.enabled,
      }),
      userInfo: (state) => state.userInfo,
    }),
    activeMenu() {
      const { path, query } = this.$route;
      if (path === '/model-config' && query.tab) {
        return `${path}?tab=${query.tab}`;
      }
      if (path === '/role-config' || path === '/device-management' || path === '/template-quick-config') {
          return '/home';
      }
      if (path === '/knowledge-file-upload') {
          return '/knowledge-base-management';
      }
      if (path === '/voice-resource-management') {
          return '/voice-clone-management';
      }
      return path;
    }
  },
  watch: {
    $route() {
      // Force update active menu if needed
    }
  },
  methods: {

    handleSelect(index) {
      if (index && index !== 'more') {
        if (this.$route.path !== index) {
          this.$router.push(index);
        }
      }
    },
    goHome() {
      if (this.$route.path !== '/home') {
        this.$router.push("/home");
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.sidebar {
  width: 240px;
  height: 100vh;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(15px);
  border-right: 1px solid rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  transition: all 0.3s ease;
  position: fixed;
  left: 0;
  top: 0;
  z-index: 1001;
  box-shadow: 4px 0 15px rgba(0, 0, 0, 0.02);
}

.sidebar-logo {
  padding: 30px 20px;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  
  .logo-img {
    height: 36px;
    width: auto;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
  }
}

.sidebar-menu {
  border-right: none;
  flex: 1;
  overflow-y: auto;
  padding: 10px 0;
  
  &::-webkit-scrollbar {
    width: 4px;
  }
  &::-webkit-scrollbar-thumb {
    background: rgba(0, 0, 0, 0.05);
    border-radius: 2px;
  }
}

::v-deep {
  .el-menu {
    border-right: none;
  }
  
  .el-menu-item, .el-submenu__title {
    height: 48px;
    line-height: 48px;
    margin: 4px 16px;
    border-radius: 12px;
    font-weight: 500;
    color: #5c637a !important;
    transition: all 0.2s ease;
    text-align: left;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    
    i {
      color: #5c637a;
      margin-right: 12px;
      font-size: 18px;
      vertical-align: middle;
    }
    
    &:hover {
      background: rgba(0, 0, 0, 0.04) !important;
      color: #000 !important;
      
      i {
          color: #000;
      }
    }
    
    &.is-active {
      background: #000 !important;
      color: #fff !important;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
      
      i {
        color: #fff;
      }
      
      span {
          color: #fff;
      }
    }
  }
  
  .el-submenu {
    &.is-active {
       .el-submenu__title {
          background: rgba(0, 0, 0, 0.02);
          color: #000 !important;
          
          i {
              color: #000;
          }
       }
    }
  }
  
  .el-submenu .el-menu-item {
    height: 40px;
    line-height: 40px;
    padding-left: 20px !important;
    margin: 2px 16px;
    font-size: 13.5px;
    
    i {
        font-size: 16px;
    }
  }
}

.sidebar-footer {
  padding: 15px;
  border-top: 1px solid rgba(0, 0, 0, 0.03);
  background: rgba(0, 0, 0, 0.01);
}
</style>
