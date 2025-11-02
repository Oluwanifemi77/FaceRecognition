import React from 'react';
import { motion } from 'framer-motion';
import { FaBrain } from 'react-icons/fa';

const Navbar = () => {
  return (
    <motion.nav
      initial={{ y: -100, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.6, type: 'spring', stiffness: 100 }}
      className="glass-dark sticky top-0 z-50 border-b border-cyan-500/20"
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <motion.div
            className="flex items-center space-x-3"
            whileHover={{ scale: 1.05 }}
            transition={{ type: 'spring', stiffness: 300 }}
          >
            <motion.div
              whileHover={{ rotate: 360, scale: 1.2 }}
              transition={{ duration: 0.6 }}
              className="relative"
            >
              <div className="absolute inset-0 bg-gradient-to-r from-cyan-500 to-purple-500 rounded-lg blur opacity-75 animate-pulse-slow"></div>
              <div className="relative bg-gradient-to-r from-cyan-500 via-purple-500 to-pink-500 p-2 rounded-lg">
                <FaBrain className="text-white text-2xl" />
              </div>
            </motion.div>
            <div>
              <motion.h1
                className="text-2xl font-bold bg-gradient-to-r from-cyan-400 via-purple-400 to-pink-400 bg-clip-text text-transparent"
                animate={{
                  backgroundPosition: ['0% 50%', '100% 50%', '0% 50%'],
                }}
                transition={{
                  duration: 5,
                  repeat: Infinity,
                  ease: 'linear',
                }}
                style={{ backgroundSize: '200% auto' }}
              >
                Emotion Recognition
              </motion.h1>
              <p className="text-xs text-cyan-400/70">AI-Powered Face Analysis</p>
            </div>
          </motion.div>

          <div className="hidden md:flex items-center space-x-6">
            {['Home', 'Upload', 'Webcam', 'About'].map((item, index) => (
              <motion.a
                key={item}
                href={`#${item.toLowerCase()}`}
                className="relative text-gray-300 hover:text-cyan-400 transition-colors font-medium group"
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.1 }}
                whileHover={{ scale: 1.1 }}
                whileTap={{ scale: 0.95 }}
              >
                {item}
                <motion.div
                  className="absolute -bottom-1 left-0 right-0 h-0.5 bg-gradient-to-r from-cyan-400 to-purple-400"
                  initial={{ scaleX: 0 }}
                  whileHover={{ scaleX: 1 }}
                  transition={{ duration: 0.3 }}
                />
              </motion.a>
            ))}
          </div>

          {/* Mobile menu indicator */}
          <motion.div
            className="md:hidden"
            whileTap={{ scale: 0.9 }}
          >
            <div className="w-6 h-5 flex flex-col justify-between cursor-pointer group">
              {[0, 1, 2].map((i) => (
                <motion.div
                  key={i}
                  className="w-full h-0.5 bg-gradient-to-r from-cyan-400 to-purple-400 rounded-full"
                  whileHover={{ scaleX: 0.8 }}
                  transition={{ delay: i * 0.05 }}
                />
              ))}
            </div>
          </motion.div>
        </div>
      </div>

      {/* Animated border bottom */}
      <motion.div
        className="h-px bg-gradient-to-r from-transparent via-cyan-500 to-transparent"
        animate={{
          opacity: [0.3, 0.7, 0.3],
        }}
        transition={{
          duration: 2,
          repeat: Infinity,
          ease: 'easeInOut',
        }}
      />
    </motion.nav>
  );
};

export default Navbar;
