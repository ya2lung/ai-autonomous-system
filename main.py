#!/usr/bin/env python3

"""

AI Autonomous System - Main Entry Point

AI mandiri dengan self-learning, reasoning, trading, coding, dan skill learning.

Powered by Ollama (Local LLM)



Author: ya2lung

Version: 0.1.0

License: MIT

"""



import asyncio

import sys

from pathlib import Path

from typing import Optional



from loguru import logger



# Add project root to path

project_root = Path(__file__).parent

sys.path.insert(0, str(project_root))



from core.brain import AIBrain

from api.server import APIServer

from config.settings import Settings





class AIAutonomousSystem:
  
    """
    
    Main AI System Orchestrator
    

    
    Mengelola seluruh komponen AI:
    
    - Core Brain (Ollama LLM)
    
    - Memory System
    
    - Trading Module
    
    - Coding Engine
    
    - Skill Learning System
    
    - Communication Interface
    
    """
  


    def __init__(self, config_path: Optional[str] = None):
      
        """Initialize AI System"""
      
        logger.info("🚀 Initializing AI Autonomous System...")
      


        # Load configuration

        self.settings = Settings(config_path)
      


        # Initialize core components

        self.brain: Optional[AIBrain] = None
      
        self.api_server: Optional[APIServer] = None
      


        logger.info("✅ AI System initialized")
      


    async def start(self):
      
        """Start AI System"""
      
        logger.info("▶️  Starting AI System...")
      


        try:
          
            # Initialize brain
          
            self.brain = AIBrain(self.settings)
          
            await self.brain.initialize()
          


            # Start API server

            self.api_server = APIServer(self.brain, self.settings)
          
            await self.api_server.start()
          


            logger.info("🎉 AI System is running!")
          
            logger.info(f"📡 API Server: http://{self.settings.api_host}:{self.settings.api_port}")
          


            # Keep running

            await self._run_forever()
          


        except Exception as e:
          
            logger.error(f"❌ Failed to start AI System: {e}")
          
            raise
          


    async def _run_forever(self):
      
        """Keep the system running"""
      
        try:
          
            while True:
              
                await asyncio.sleep(1)
              
        except asyncio.CancelledError:
          
            logger.info("⏹️  AI System shutting down...")
          


    async def stop(self):
      
        """Stop AI System gracefully"""
      
        logger.info("🛑 Stopping AI System...")
      


        if self.api_server:
          
            await self.api_server.stop()
          


        if self.brain:
          
            await self.brain.shutdown()
          


        logger.info("👋 AI System stopped")
      




def print_banner():
  
    """Print welcome banner"""
  
    banner = """
    
    ╔═══════════════════════════════════════════════════════════╗
    
    ║                                                           ║
    
    ║   🤖 AI AUTONOMOUS SYSTEM 🤖                             ║
    
    ║                                                           ║
    
    ║   Self-Learning • Reasoning • Trading • Coding           ║
    
    ║   Skill Learning • 2-Way Communication                   ║
    
    ║                                                           ║
    
    ║   Powered by Ollama (Local LLM)                          ║
    
    ║   Version: 0.1.0 | License: MIT                          ║
    
    ║                                                           ║
    
    ╚═══════════════════════════════════════════════════════════╝
    
    """
  
    print(banner)
  




async def main():
  
    """Main entry point"""
  
    print_banner()
  


    # Initialize and start AI

    ai = AIAutonomousSystem()
  


    try:
      
        await ai.start()
      
    except KeyboardInterrupt:
      
        logger.info("👋 Interrupted by user")
      
    finally:
      
        await ai.stop()
      




if __name__ == "__main__":
  
    # Configure logging
  
    logger.remove()
  
    logger.add(
      
        sys.stderr,
      
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
      
        level="INFO",
      
        colorize=True
      
    )
  
    logger.add(
      
        "logs/ai_system.log",
      
        rotation="10 MB",
      
        retention="30 days",
      
        level="DEBUG"
      
    )
  


    # Run main loop

    asyncio.run(main())



























































































